def main():
    text_file = "books/frankenstein.txt"
    text = get_text_contents(text_file)
    char_dict = count_characters(text)
    print(char_dict)
    

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


main()