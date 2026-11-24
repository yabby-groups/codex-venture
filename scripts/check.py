import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else 'dist')


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links, self.ids = [], set()
        self.title = self.canonical = self.lang = None
        self.read_title = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
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
        if tag == 'title':
            self.read_title = False

    def handle_data(self, data):
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
    canonicals = set()
    titles = set()
    for path, page in pages.items():
        if not page.title or page.title in titles or page.lang != 'zh-CN' or not page.canonical:
            raise ValueError(f'{path}: missing metadata or duplicate title')
        if page.canonical in canonicals or urlsplit(page.canonical).hostname != 'codex-venture.com':
            raise ValueError(f'{path}: duplicate or invalid canonical URL')
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
            if not destination.is_file():
                raise ValueError(f'{path}: missing {link}')
            if url.fragment and destination in pages and unquote(url.fragment) not in pages[destination].ids:
                raise ValueError(f'{path}: missing anchor {link}')
    for filename in ['rss.xml', 'sitemap-index.xml', *[p.name for p in ROOT.glob('sitemap-*.xml') if p.name != 'sitemap-index.xml']]:
        tree = ElementTree.parse(ROOT / filename)
        for entry in tree.iter():
            if entry.tag.split('}')[-1] in ('loc', 'link') and entry.text and entry.text.startswith('https://codex-venture.com'):
                if not target(urlsplit(entry.text).path).is_file():
                    raise ValueError(f'{filename}: missing {entry.text}')
    print(f'Checked {len(pages)} HTML pages, internal links, metadata, RSS, sitemap and Pagefind')


if __name__ == '__main__':
    check()
