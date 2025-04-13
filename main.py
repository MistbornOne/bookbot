#use sys in command line to allow any book path to be analyzed
import sys

#import functions from stats file
from stats import get_num_words
from stats import get_num_char
from stats import chars_dict_to_sorted_list

#create the main function, in which all else will be housed
#main takes the book path and gets the text from the book as a string
def main():
    # Check if command line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) #exit with status code 1 to indicate error
    #book_path = sys.argv[1]

    # Process each file path provided in command line arguments
    for book_path in sys.argv[1:]:
        try:
            text = get_book_text(book_path)
            num_words = get_num_words(text)
            num_chars = get_num_char(text)
            chars_sorted_list = chars_dict_to_sorted_list(num_chars)
            print_report(book_path, num_words, chars_sorted_list)
        except FileNotFoundError:
            print(f"Error: File '{book_path}' not found.")
        except Exception as e:
            print(f"Error processing '{book_path}': {str(e)}")

        # Add a separator between multiple file reports
        if book_path != sys.argv[-1]:
            print("\n" + "="*35 + "\n")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in chars_sorted_list:
            if not item["char"].isalpha():
                continue
            print(f"{item['char']}: {item['num']}")

        print("============= END ===============")
    #return text




main()
