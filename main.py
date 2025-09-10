import sys

from stats import get_character_stats
from stats import print_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    argv = sys.argv
    if len(argv) != 2:
        raise Exception('Usage: python3 main.py <path_to_book>')
    else:
        path = argv[1]
        content = get_book_text(path)
        stats = get_character_stats(content)
        print_report(stats)

main()
