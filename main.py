from stats import count_words

def get_book_text(path):
    text = ''
    with open(path) as f:
        text = f.read()

    return text

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    word_count = count_words(book_text)

    print(f"{word_count} words found in the document")

main()
