


def count_words(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        return len(file_contents.split())

def count_of_each_letter(file_name):
    with open(file_name) as f:
        file_contents = f.read()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_dict = {}
    file_contents = file_contents.lower()

    for letter in alphabet:
        letter_dict[letter] = file_contents.count(letter)
    
    return letter_dict




def main():
    file_name = "books/frankenstein.txt"
    word_count = count_words(file_name)
    letter_counts = count_of_each_letter(file_name)
    letter_count_list = []

    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words foun in the document")
    print()
    
    for key in letter_counts.keys():
        letter_count_list.append([key,letter_counts[key]])

    letter_count_list.sort()

    for letter in letter_count_list:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    
    print("--- End report ---")

main()