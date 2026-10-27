"""Publish home/ to the root of the gh-pages branch.

home/ holds what docs.sodero.io serves outside the product manuals: the product home page,
the not-found page (which also forwards old Stellar X addresses), CNAME, robots.txt, the sitemap
index and llms.txt. The manuals under /sodero-cloud/ and /stellar-x/ are deployed by mike and are
not touched here.

    python3 tools/publish_home.py            # commit to the local gh-pages branch
    python3 tools/publish_home.py --push     # and push it
"""
import argparse

from pages import commit, copy_home, git, worktree


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--branch', default='gh-pages', help='pages branch (default: gh-pages)')
    parser.add_argument('--remote', default='origin', help='remote to push to (default: origin)')
    parser.add_argument('--push', action='store_true', help='push the branch after committing')
    args = parser.parse_args()

    with worktree(args.branch) as path:
        files = copy_home(path)
        git('add', '--', *files, cwd=path)
        changed = commit(path, 'Update the docs.sodero.io home page')
        print('home page updated' if changed else 'home page unchanged')
        if args.push:
            git('push', '--quiet', args.remote, args.branch, cwd=path)


if __name__ == '__main__':
    main()
