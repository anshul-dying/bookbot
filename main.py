from stats import count_words, num_letters_in_text, sorted_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    path = sys.argv[1]
    content = get_book_text(path)
    num_words = count_words(content)
    letters = num_letters_in_text(content)
    
    sorted_letters_dict:dict = sorted_dict(letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------\n"
          f"Found {num_words} total words\n"
          f"--------- Character Count -------")
    for key, value in sorted_letters_dict.items():
        print(f"{key}: {value}")

    print("============= END ===============")

main()