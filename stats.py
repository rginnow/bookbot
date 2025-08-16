def sort_by_count(items):
    return items["count"]

def count_words(text):
    return len(text.split())

def count_character_usage(text):
    character_list = list(text)

    character_dict = {}
    for c in character_list:
        character = c.lower()
        if character in character_dict:
            character_dict[character] = character_dict[character] + 1
        else:
            character_dict[character] = 1

    return character_dict

def sort_character_usage_by_count(usage_dict):
    character_list = list(usage_dict)

    dict_list = []
    for c in character_list:
        if c.isalpha():
            count = usage_dict[c]
            dict_list.append({"char": c, "count": count})

    dict_list.sort(reverse=True, key=sort_by_count)
    return dict_list
