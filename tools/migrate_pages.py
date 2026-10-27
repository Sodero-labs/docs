"""Move the Stellar X manual from the root of the gh-pages branch to /stellar-x/ (run once).

Before the split by product, mike deployed the Stellar X versions at the root:
/v1.0.0/, /v1.0.1/, /v2.0.0/, the alias /latest, /versions.json and /index.html.
This script moves them under /stellar-x/ so that mike can deploy each product with its own
prefix, and keeps the old addresses working:

- every page of the old folders gets a small redirect page to the same page under /stellar-x/;
- 404.html (from home/) forwards any other old address, such as a download, the same way;
- each moved version gets the current javascripts/version.js, so its version menu reads
  /stellar-x/versions.json.

The leftovers of the first, unversioned deployment at the root (assets/, javascripts/, styles/,
overrides/, stellarx/, sitemap and llms files) are removed, and home/ is published to the root.

    python3 tools/migrate_pages.py                    # commit to the local gh-pages branch
    python3 tools/migrate_pages.py --branch preview   # try it on a copy of the branch
    python3 tools/migrate_pages.py --push             # commit and push
"""
import argparse
import json
import os
import shutil

from pages import ROOT, commit, copy_home, git, worktree

PRODUCT = 'stellar-x'
VERSION_JS = ROOT / 'shared' / 'theme' / 'javascripts' / 'version.js'
LEFTOVERS = ['versions.json', 'index.html', '404.html', 'assets', 'javascripts', 'styles', 'overrides',
             'stellarx', 'llms.txt', 'llms-full.txt', 'sitemap.xml', 'sitemap.xml.gz']
REDIRECT = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Redirecting</title>
  <link rel="canonical" href="https://docs.sodero.io{url}">
  <meta http-equiv="refresh" content="0; url={url}">
  <script>window.location.replace("{url}" + window.location.search + window.location.hash);</script>
</head>
<body>This page has moved to <a href="{url}">{url}</a>.</body>
</html>
'''


def page_url(rel):
    """The address of a built page: a/b/index.html -> a/b/, index.html -> '', a.html -> a.html."""
    if rel == 'index.html':
        return ''
    if rel.endswith('/index.html'):
        return rel[:-len('index.html')]
    return rel


def write_redirects(root, old, new):
    """Write a redirect page at /<old>/<page> for every page of /<PRODUCT>/<new>/."""
    count = 0
    for page in (root / PRODUCT / new).rglob('*.html'):
        rel = page.relative_to(root / PRODUCT / new).as_posix()
        if rel == '404.html':
            continue
        target = root / old / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(REDIRECT.format(url=f'/{PRODUCT}/{old}/{page_url(rel)}'))
        count += 1
    return count


def migrate(root):
    versions = json.loads((root / 'versions.json').read_text())
    (root / PRODUCT).mkdir(exist_ok=True)

    for entry in versions:
        version = entry['version']
        git('mv', version, f'{PRODUCT}/{version}', cwd=root)
        shutil.copy2(VERSION_JS, root / PRODUCT / version / 'javascripts' / 'version.js')
        for alias in entry.get('aliases', []):
            git('rm', '--quiet', alias, cwd=root)
            os.symlink(version, root / PRODUCT / alias)
    (root / PRODUCT / 'versions.json').write_text(json.dumps(versions, indent=2) + '\n')
    shutil.copy2(root / 'index.html', root / PRODUCT / 'index.html')

    for name in LEFTOVERS:
        if (root / name).exists() or (root / name).is_symlink():
            git('rm', '-r', '--quiet', name, cwd=root)

    pages = 0
    for entry in versions:
        pages += write_redirects(root, entry['version'], entry['version'])
        for alias in entry.get('aliases', []):
            pages += write_redirects(root, alias, entry['version'])

    copy_home(root)
    git('add', '--all', '.', cwd=root)
    print(f'moved {len(versions)} versions to /{PRODUCT}/, wrote {pages} redirect pages')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--branch', default='gh-pages', help='pages branch (default: gh-pages)')
    parser.add_argument('--remote', default='origin', help='remote to push to (default: origin)')
    parser.add_argument('--push', action='store_true', help='push the branch after committing')
    args = parser.parse_args()

    with worktree(args.branch) as root:
        if (root / PRODUCT).exists():
            raise SystemExit(f'/{PRODUCT}/ already exists on {args.branch}: nothing to migrate')
        migrate(root)
        commit(root, 'Move the Stellar X manual to /stellar-x/ and add the product home page')
        if args.push:
            git('push', '--quiet', args.remote, args.branch, cwd=root)


if __name__ == '__main__':
    main()
