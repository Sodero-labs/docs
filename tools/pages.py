"""Helpers for scripts that change the gh-pages branch through a temporary worktree."""
import contextlib
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / 'home'


def git(*args, cwd=ROOT):
    return subprocess.run(['git', *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


@contextlib.contextmanager
def worktree(branch):
    """Check out `branch` in a temporary folder and remove the folder afterwards."""
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / 'pages'
        git('worktree', 'add', '--quiet', str(path), branch)
        try:
            yield path
        finally:
            git('worktree', 'remove', '--force', str(path))


def copy_home(dest):
    """Copy every file of home/ to the root of `dest`; return the copied paths."""
    copied = []
    for src in sorted(p for p in HOME.rglob('*') if p.is_file()):
        rel = src.relative_to(HOME)
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target)
        copied.append(rel.as_posix())
    return copied


def commit(path, message):
    """Commit what is staged in `path`; return False when nothing changed."""
    if subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=path).returncode == 0:
        return False
    git('commit', '--quiet', '-m', message, cwd=path)
    return True
