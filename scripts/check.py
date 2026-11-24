import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

from geo import SITE, robot_groups

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else 'dist')


class Page(HTMLParser):
    def __init__(self, path=None, *, markup=None):
        super().__init__()
        self.links, self.ids = [], set()
        self.title = self.canonical = self.lang = None
        self.read_title = False
        self.noindex = False
        self.schemas = []
        self.schema_text = None
        self.tags = Counter()
        self.languages = set()
        self.feed(path.read_text() if markup is None else markup)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags[tag] += 1
        if attrs.get('lang'):
            self.languages.add(attrs['lang'])
        if tag == 'meta' and attrs.get('name', '').lower() in ('robots', 'googlebot', 'bingbot'):
            self.noindex |= bool(re.search(r'\b(noindex|nosnippet|none)\b', attrs.get('content', '').lower()))
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.schema_text = ''
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'title':
            self.read_title = True
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])

    def handle_endtag(self, tag):
        if tag == 'script' and self.schema_text is not None:
            self.schemas.append(json.loads(self.schema_text))
            self.schema_text = None
        if tag == 'title':
            self.read_title = False

    def handle_data(self, data):
        if self.schema_text is not None:
            self.schema_text += data
        if self.read_title:
            self.title = (self.title or '') + data


def target(path):
    path = ROOT / unquote(path).lstrip('/')
    return path / 'index.html' if path.is_dir() else path


def check():
    pages = {path: Page(path) for path in ROOT.rglob('*.html')}
    for mandatory in ('index.html', 'daily/index.html', 'news/index.html', 'tags/index.html', 'archive/index.html',
                      'search/index.html', 'about/index.html', 'robots.txt', 'pagefind/pagefind.js'):
        if not (ROOT / mandatory).is_file():
            raise ValueError(f'missing {mandatory}')
    robot_groups((ROOT / 'robots.txt').read_text(), require_sitemap=True)
    canonicals = set()
    indexable = set()
    inbound = set()
    articles = set()
    titles = set()
    for path, page in pages.items():
        if not page.title or page.title in titles or page.lang != 'zh-CN' or not page.canonical:
            raise ValueError(f'{path}: missing metadata or duplicate title')
        if page.canonical in canonicals or urlsplit(page.canonical).hostname != 'codex-venture.com':
            raise ValueError(f'{path}: duplicate or invalid canonical URL')
        is_excluded = path.relative_to(ROOT).as_posix() in ('404.html', 'search/index.html')
        if not is_excluded:
            indexable.add(page.canonical)
            if page.noindex or target(urlsplit(page.canonical).path) != path:
                raise ValueError(f'{path}: unexpected robots or canonical')
        if page.tags['main'] != 1 or page.tags['h1'] != 1:
            raise ValueError(f'{path}: expected one main and h1')
        if re.fullmatch(r'(news|daily)/[^/]+/index.html', path.relative_to(ROOT).as_posix()):
            articles.add(path)
            schema = next((value for value in page.schemas if value.get('headline')), {})
            if (page.tags['article'] != 1 or not {'zh-CN', 'en'} <= page.languages or
                schema.get('mainEntityOfPage') != page.canonical or
                not schema.get('citation') or any(url not in page.links for url in schema['citation'])):
                raise ValueError(f'{path}: article language, semantics or JSON-LD mismatch')
        titles.add(page.title)
        canonicals.add(page.canonical)
        for link in page.links:
            url = urlsplit(link)
            if url.netloc or url.scheme:
                continue
            if url.path.startswith('/'):
                destination = target(url.path)
            elif url.path:
                destination = (path.parent / unquote(url.path)).resolve()
                if destination.is_relative_to(ROOT.resolve()):
                    destination = target('/' + destination.relative_to(ROOT.resolve()).as_posix())
            else:
                destination = path
            if path != destination:
                inbound.add(destination)
            if not destination.is_file():
                raise ValueError(f'{path}: missing {link}')
            if url.fragment and destination in pages and unquote(url.fragment) not in pages[destination].ids:
                raise ValueError(f'{path}: missing anchor {link}')
    if articles - inbound:
        raise ValueError(f'Orphan articles: {sorted(articles - inbound)}')
    sitemap_urls = []
    for filename in ['rss.xml', 'sitemap-index.xml', *[p.name for p in ROOT.glob('sitemap-*.xml') if p.name != 'sitemap-index.xml']]:
        tree = ElementTree.parse(ROOT / filename)
        if filename.startswith('sitemap-') and filename != 'sitemap-index.xml':
            sitemap_urls.extend(node.text for node in tree.findall('.//{*}loc'))
        for entry in tree.iter():
            if entry.tag.split('}')[-1] in ('loc', 'link') and entry.text and entry.text.startswith('https://codex-venture.com'):
                if not target(urlsplit(entry.text).path).is_file():
                    raise ValueError(f'{filename}: missing {entry.text}')
    if set(sitemap_urls) != indexable or len(sitemap_urls) != len(indexable):
        raise ValueError(f'Sitemap coverage mismatch: {set(sitemap_urls) ^ indexable}')
    for link in re.findall(r'\]\((https://[^)]+)\)', (ROOT / 'llms.txt').read_text()):
        if not link.startswith(SITE + '/') or not target(urlsplit(link).path).is_file():
            raise ValueError(f'Invalid llms.txt link: {link}')
    print(f'Checked {len(pages)} HTML pages, internal links, metadata, RSS, sitemap and Pagefind')


if __name__ == '__main__':
    check()
