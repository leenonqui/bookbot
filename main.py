global frankenstein
frankenstein = './books/frankenstein.txt'

def get_book_txt(filepath):
    with open(filepath) as file:
        txt = file.read()
    return txt

def get_words_count(txt):
    words = txt.split()
    return len(words)

def get_chars_dict(txt):
    lower_txt = txt.lower()
    dict = {}

    for char in lower_txt:
        if char in dict.keys():
            dict[char] += 1
        else: dict[char] = 1

    return dict

def get_report(book):
    char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    txt = get_book_txt(book)
    word_count = get_words_count(txt)
    chars_dict = get_chars_dict(txt)
    # sort dict by values in descending order
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse = True))

    intro = f"--- Begin report of {book} ---\n"
    word_str = f"{word_count} were found in the document\n"
    conlusion = "\n--- End Report ---"

    report = intro + word_str

    for char in sorted_dict:
        if char in char_list:
            report += f"\nThe '{char}' character was found {chars_dict[char]} times"

    report += conlusion

    return report

def main():
    frankenstein_report = get_report(frankenstein)
    print(frankenstein_report)

main()
