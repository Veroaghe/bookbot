def main():
    text_file = "books/frankenstein.txt"
    create_report(text_file)
    

def get_text_contents(text_file):
    with open(text_file) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_dict = {}

    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict


def convert_dict_to_list_of_dicts(dict):
    L = []
    for key in dict:
        L.append({"char" : key, "count" : dict[key]})
    return L


def create_report(text_file, sort_method="count"):
    text = get_text_contents(text_file)
    char_dict = count_characters(text)
    word_count = count_words(text)

    def sort_on(dict, key=sort_method):
        return dict[key]

    char_list = convert_dict_to_list_of_dicts(char_dict)
    char_list.sort(key=sort_on)

    print(f"--- Begin report of {text_file} ---")
    print(f"{word_count} words found in the document\n")

    for d in char_list:
        if str.isalpha(d["char"]):
            print(f"The '{d['char']}' character was found {d['count']} times")

    print("--- End report ---")


main()