
#open file and return contents
def read_file(file_name):
    try:
        with open(file_name) as f:
            return f.read()
    except FileNotFoundError:
        print(f"'{file_name}' not found")
    except:
        print(f"Something else went wrong opening '{file_name}'")

#input file contents and return sum of words
def count_words(file_contents):
    return len(file_contents.split())

#input file contents and returns list of [letter, count] lists sorted by count desc
def count_of_each_letter(file_contents):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_counts = []
    file_contents = file_contents.lower()

    for letter in alphabet:
        letter_counts.append([letter, file_contents.count(letter)])
    
    letter_counts = sorted(letter_counts,reverse = True,key = sort_key)

    return letter_counts

#sort key for list of letter lists
def sort_key(x):
	return x[1]

#print report
def print_report(file_name,word_count,letter_counts):
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words foun in the document")
    print()
    for letter in letter_counts:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")

def main():
    file_name = "bookbot/books/frankenstein.txt"
    file_contents = read_file(file_name)
    if file_contents is not None and len(file_contents) > 0:
        word_count = count_words(file_contents)
        letter_counts = count_of_each_letter(file_contents)
        print_report(file_name,word_count,letter_counts)
    else:
        print("File is empty")

main()