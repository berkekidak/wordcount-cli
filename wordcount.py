import argparse
from pathlib import Path

def count_text(text: str) -> tuple[int, int, int]:
    lines = text.splitlines()
    words = text.split()
    chars = list(text)
    return (len(lines), len(words), len(chars))

def main() -> int:
    parser = argparse.ArgumentParser(description="Count lines, words, and characters in a text file.")
    parser.add_argument("path", help="Path to a text file")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"Error: file not found: {path}")
        return 1
    if path.is_dir():
        print(f"Error: path is a directory: {path}")
        return 1

    text = path.read_text(encoding="utf-8", errors="replace")
    lines, words, chars = count_text(text)

    print(f"File: {path.name}")
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Chars: {chars}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())