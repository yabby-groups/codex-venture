import hashlib
import os
import shutil
import subprocess
import time
import urllib.request
from pathlib import Path

from collect import load, save

RUNTIME = Path('.venture-runtime')
JOURNAL = RUNTIME / 'release.json'
ROUTES = ('', 'daily/', 'news/', 'search/', 'rss.xml', 'sitemap-index.xml',
          'pagefind/pagefind.js', 'release.txt')
TRACKED = ('src/content', 'state', 'config/sources.yaml')


def run(*command, timeout=120, **kwargs):
    return subprocess.run(command, check=True, timeout=timeout, **kwargs)


def tree_hash(root):
    digest = hashlib.sha256()
    for path in sorted(root.rglob('*')):
        if path.is_file() and path.name != 'release.txt':
            digest.update(path.relative_to(root).as_posix().encode() + b'\0')
            digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def point(root, target):
    current = root / 'current'
    if target is None:
        current.unlink(missing_ok=True)
        return
    temporary = root / '.next'
    temporary.unlink(missing_ok=True)
    temporary.symlink_to(target)
    temporary.replace(current)


def probe(base, release, routes=ROUTES):
    for route in routes:
        url = base.rstrip('/') + '/' + route
        request = urllib.request.Request(url, headers={'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(request, timeout=8) as response:
            if response.status != 200:
                raise RuntimeError(f'{url}: unexpected HTTP {response.status}')
            if route == 'release.txt' and response.read(256).decode().strip() != release:
                raise RuntimeError(f'{url}: release marker mismatch')


def recover():
    if not JOURNAL.exists():
        return
    transaction = load(JOURNAL, {})
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    if revision == transaction['before']:
        point(Path(transaction['root']), transaction['previous'])
        run('git', 'reset', '--quiet', 'HEAD', '--', *TRACKED)
    JOURNAL.unlink()


def commit():
    changes = subprocess.check_output(['git', 'status', '--porcelain', '--', *TRACKED], text=True)
    if not changes:
        return
    run('git', 'add', '--', *TRACKED)
    try:
        status = subprocess.run(['git', 'diff', '--cached', '--quiet'], check=False).returncode
        if status == 1:
            run('git', 'commit', '-m', 'Update Codex Venture editorial index and content')
        elif status:
            raise RuntimeError('could not determine staged changes')
    except BaseException:
        run('git', 'reset', '--quiet', 'HEAD', '--', *TRACKED)
        raise


def release(build=True, record=True):
    base = os.environ['VENTURE_SITE_URL']
    root = Path(os.environ['VENTURE_DEPLOY_ROOT']).resolve()
    if build:
        run('npm', 'run', 'build', timeout=240, env={**os.environ, 'ASTRO_TELEMETRY_DISABLED': '1'})
    dist = Path('dist')
    release_id = tree_hash(dist)
    (dist / 'release.txt').write_text(release_id + '\n')
    releases = root / 'releases'
    releases.mkdir(parents=True, exist_ok=True)
    destination = releases / release_id
    if not destination.exists():
        temporary = releases / '.staging'
        if temporary.exists():
            shutil.rmtree(temporary)
        shutil.copytree(dist, temporary)
        temporary.rename(destination)
    if tree_hash(destination) != release_id or (destination / 'release.txt').read_text().strip() != release_id:
        raise RuntimeError('existing release failed integrity check')
    old = os.readlink(root / 'current') if (root / 'current').is_symlink() else None
    if record:
        before = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
        save(JOURNAL, dict(root=str(root), previous=old, before=before))
    try:
        point(root, f'releases/{release_id}')
        for attempt in range(3):
            try:
                articles = tuple(path.parent.relative_to(dist).as_posix() + '/' for directory in ('news', 'daily')
                                 for path in (dist / directory).glob('*/index.html'))
                probe(base, release_id, (*ROUTES, *articles))
                break
            except (OSError, RuntimeError):
                if attempt == 2:
                    raise
                time.sleep(2)
        if record:
            commit()
    except BaseException:
        point(root, old)
        JOURNAL.unlink(missing_ok=True)
        raise
    JOURNAL.unlink(missing_ok=True)
    for path in sorted((p for p in releases.iterdir() if p.is_dir() and len(p.name) == 64),
                       key=lambda p: p.stat().st_mtime, reverse=True)[5:]:
        if path.name not in (release_id, Path(old or '.').name):
            shutil.rmtree(path)
    print(f'Published {release_id} and verified {base}')
