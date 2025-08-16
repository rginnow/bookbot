from stats import count_words, count_character_usage, sort_character_usage_by_count

def get_book_text(path):
    text = ''
    with open(path) as f:
        text = f.read()

    return text

def report_header(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")

def report_word_count(count):
    print("----------- Word Count ----------")
    print(f"Found {count} total words")

def report_character_count(character_list):
    print("--------- Character Count -------")
    for item in character_list:
        character = item["char"]
        count = item["count"]
        print(f"{character}: {count}")

def report_footer():
    print("============= END ===============")

def main():
    path = "books/frankenstein.txt"

    book_text = get_book_text(path)
    word_count = count_words(book_text)
    char_count = count_character_usage(book_text)
    char_usage = sort_character_usage_by_count(char_count)

    report_header(path)
    report_word_count(word_count)
    report_character_count(char_usage)
    report_footer()

main()
