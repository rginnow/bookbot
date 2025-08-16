def count_words(text):
    return len(text.split())

def count_character_usage(text):
    char_list = list(text)
    char_count = len(char_list)

    characters = {}
    for i in range(char_count):
        char = char_list[i].lower()
        if char in characters:
            characters[char] = characters[char] + 1
        else:
            characters[char] = 1

    return characters
