import sys
from stats import get_num_words, get_num_chars_sorted

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path =sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...\n")

    # Lese das Buch
    with open(path, "r") as f:
        text = f.read()

    # Wortanzahl berechnen
    word_count = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words\n")

    # Zeichenhäufigkeit berechnen (sortierte Liste)
    sorted_chars = get_num_chars_sorted(text)

    print("-------- Character Count --------")
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")

    print("============ END ================")

if __name__ == "__main__":
    main()

