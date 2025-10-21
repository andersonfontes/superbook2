# dump_project.py
import os
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))
OUTFILE = os.path.join(ROOT, "superbook_project_dump.txt")

SKIP_DIRS = {
    ".git", ".hg", ".svn", ".idea", ".vscode", "__pycache__",
    "venv", "env", ".venv", "node_modules", "dist", "build",
    ".mypy_cache", ".pytest_cache", ".ruff_cache"
}
SKIP_FILES = {
    "db.sqlite3",
}
BINARY_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".bmp", ".pdf",
    ".zip", ".gz", ".tar", ".rar", ".7z", ".woff", ".woff2",
    ".ttf", ".eot", ".pyc", "migrations"
}

def is_binary(path: str) -> bool:
    _, ext = os.path.splitext(path.lower())
    return ext in BINARY_EXTS

def should_skip_dir(path: str) -> bool:
    return os.path.basename(path) in SKIP_DIRS

def should_skip_file(path: str) -> bool:
    name = os.path.basename(path)
    if name in SKIP_FILES:
        return True
    if is_binary(path):
        return True
    return False

def main():
    files_dumped = 0
    with open(OUTFILE, "w", encoding="utf-8", errors="ignore") as out:
        out.write("# DUMP DO PROJETO\n")
        out.write(f"# Raiz: {ROOT}\n\n")
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames if not should_skip_dir(os.path.join(dirpath, d))]
            for fn in filenames:
                full = os.path.join(dirpath, fn)
                if os.path.abspath(full) == os.path.abspath(__file__):
                    continue
                if should_skip_file(full):
                    continue
                rel = os.path.relpath(full, ROOT)
                out.write("\n" + "="*90 + "\n")
                out.write(f"# FILE: {rel}\n")
                out.write("="*90 + "\n")
                try:
                    with open(full, "r", encoding="utf-8", errors="ignore") as f:
                        out.write(f.read())
                except Exception as e:
                    out.write(f"\n[ERRO AO LER {rel}: {e}]\n")
                out.write("\n")
                files_dumped += 1
    print(f"OK: dump gerado em {OUTFILE} com {files_dumped} arquivos.")

if __name__ == "__main__":
    sys.exit(main())
