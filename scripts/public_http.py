"""Bounded HTTPS transport for untrusted collection URLs."""

import http.client
import ipaddress
import socket
import time
from urllib.error import HTTPError
from urllib.parse import urljoin, urlsplit


def public_addresses(url):
    parts = urlsplit(url)
    if (parts.scheme != 'https' or not parts.hostname or parts.username is not None
            or parts.password is not None or parts.port not in (None, 443)
            or any(ord(char) <= 32 or char == '\\' for char in url)):
        raise ValueError('expected a public HTTPS URL on port 443')
    addresses = socket.getaddrinfo(parts.hostname, 443, type=socket.SOCK_STREAM)
    for _, _, _, _, address in addresses:
        ip = ipaddress.ip_address(address[0])
        ip = getattr(ip, 'ipv4_mapped', None) or ip
        if not ip.is_global or ip.is_multicast or ip.is_reserved or getattr(ip, 'is_site_local', False):
            raise ValueError('non-public DNS result')
    return parts, addresses


def connect_pinned(addresses, timeout):
    last_error = None
    for family, socktype, protocol, _, address in addresses:
        sock = socket.socket(family, socktype, protocol)
        sock.settimeout(timeout)
        try:
            sock.connect(address)
            return sock
        except OSError as error:
            sock.close()
            last_error = error
    raise last_error or OSError('no public address')


def request(url, headers, max_bytes=4_000_000, before_request=None, after_request=None):
    deadline = time.monotonic() + 18
    for _ in range(4):
        parts, addresses = public_addresses(url)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError('HTTPS deadline exceeded')
        connection = http.client.HTTPSConnection(parts.hostname, timeout=min(6, remaining))
        # Preserve TLS verification and SNI while connecting to the checked IP.
        connection._create_connection = lambda address, timeout, source: connect_pinned(addresses, timeout)
        path = parts.path or '/'
        if parts.query:
            path += '?' + parts.query
        try:
            if before_request:
                before_request(parts.hostname)
            connection.request('GET', path, headers=headers)
            with connection.getresponse() as response:
                status, response_headers = response.status, response.headers
                if after_request:
                    after_request(parts.hostname, status, response_headers)
                if status in (301, 302, 303, 307, 308) and response_headers.get('Location'):
                    url = urljoin(url, response_headers['Location'])
                    headers = {key: value for key, value in headers.items() if key.lower() == 'user-agent'}
                    from collect import robots, AGENT
                    target, _ = public_addresses(url)
                    if path != '/robots.txt' and not robots(f'https://{target.netloc}').can_fetch(AGENT, url):
                        raise ValueError('redirect blocked by robots.txt')
                    continue
                if status == 304 or not 200 <= status < 300:
                    raise HTTPError(url, status, response.reason, response_headers, None)
                body = bytearray()
                while len(body) <= max_bytes:
                    if time.monotonic() >= deadline:
                        raise TimeoutError('response deadline exceeded')
                    chunk = response.read1(min(65536, max_bytes + 1 - len(body)))
                    if not chunk:
                        return bytes(body), response_headers
                    body.extend(chunk)
                raise ValueError('response exceeds byte limit')
        finally:
            connection.close()
    raise ValueError('too many redirects')
