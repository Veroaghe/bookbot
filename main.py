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


def in_alphabet(char):
    return ord(char.lower()) in range(ord('a'), ord('z') + 1)


def create_report(text_file):
    text = get_text_contents(text_file)
    char_dict = count_characters(text)
    word_count = count_words(text)

    print(f"--- Begin report of {text_file} ---")
    print(f"{word_count} words found in the document\n")

    for char in char_dict:
        if in_alphabet(char):
            print(f"The '{char}' character was found {char_dict[char]} times")

    print("--- End report ---")


main()