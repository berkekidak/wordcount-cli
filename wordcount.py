import argparse
import sys
from pathlib import Path

__version__ = "0.1.0"


def count_text(text: str) -> tuple[int, int, int]:
    lines = text.count("\n") + (0 if text == "" else 1)
    words = len(text.split())
    chars = len(text)
    return lines, words, chars


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print line, word, and character counts for a text file."
    )
    parser.add_argument("file", help="Path to the text file")
    parser.add_argument(
        "--lines",
        action="store_true",
        help="Show only the line count",
    )
    parser.add_argument(
        "--words",
        action="store_true",
        help="Show only the word count",
    )
    parser.add_argument(
        "--chars",
        action="store_true",
        help="Show only the character count",
    )

    args = parser.parse_args()
    file_path = Path(args.file)

    if not file_path.is_file():
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    
    text = file_path.read_text(encoding="utf-8")
    lines, words, chars = count_text(text)

    if args.lines:
        print(lines)
    elif args.words:
        print(words)
    elif args.chars:
        print(chars)
    else:
        print("=" * 28)
        print(f"File   : {args.file}")
        print(f"Lines  : {lines}")
        print(f"Words  : {words}")
        print(f"Chars  : {chars}")
        print("=" * 28)
        


if __name__ == "__main__":
    main()
