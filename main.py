from stats import count_words, count_character_usage

def get_book_text(path):
    text = ''
    with open(path) as f:
        text = f.read()

    return text

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    print(count_character_usage(book_text))

main()
