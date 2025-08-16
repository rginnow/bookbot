# Count the number of words in the book
# text is the full text content of the book
def count_words(text):
    return len(text.split())

# Count the number of times a character is used in the book
# text is the full text content of the book
def count_character_usage(text):
    character_list = list(text)
    character_dict = {}

    # Loop each character in the book text
    # and append it to the dictonary if it doesn't exist
    # or increase its count value by 1 if it already does
    for c in character_list:
        character = c.lower()
        if character in character_dict:
            character_dict[character] = character_dict[character] + 1
        else:
            character_dict[character] = 1

    return character_dict

# Define the key to sort by in the list of dictionaries
# item is a dictonary
def sort_by_count(item):
    return item["count"]

# Get the count of characters, sorted from high to low
# usage_dict is a dictonary of <character>: <count>
def sort_character_usage_by_count(usage_dict):
    character_list = list(usage_dict)
    dict_list = []

    # Loop each character in the list
    # and append the specific dictionary structure to the list
    for c in character_list:
        if c.isalpha():
            count = usage_dict[c]
            dict_list.append({"char": c, "count": count})

    dict_list.sort(reverse=True, key=sort_by_count)
    return dict_list
