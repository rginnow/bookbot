import sys
from stats import count_words, count_character_usage, sort_character_usage_by_count

# Get the contents found at the path provided
def get_book_text(path):
    text = ''
    with open(path) as f:
        text = f.read()

    return text

# Print the BookBot header
# path is a string of the relative path to the book
def report_header(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")

# Print the word count section
# count is an integer of the total words in the book
def report_word_count(count):
    print("----------- Word Count ----------")
    print(f"Found {count} total words")

# Print the character count section
# character_list is a list of dictionaries of each character's total count
def report_character_count(character_list):
    print("--------- Character Count -------")

    # Loop each dictionary in the list
    for item in character_list:
        character = item["char"]
        count = item["count"]
        print(f"{character}: {count}")

# End the report
def report_footer():
    print("============= END ===============")

def main():
    # If we don't get 2 arguments, show command usage
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get path from arguments
    path = sys.argv[1]

    # Gather data about the book from the path
    book_text = get_book_text(path)
    word_count = count_words(book_text)
    char_count = count_character_usage(book_text)
    char_usage = sort_character_usage_by_count(char_count)

    # Build the report
    report_header(path)
    report_word_count(word_count)
    report_character_count(char_usage)
    report_footer()

main()
