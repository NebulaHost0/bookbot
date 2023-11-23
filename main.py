def main():
    path_to_book = "books/frankenstein.txt"
    text = read_book(path_to_book)
    num_words = count_words(text)
    num_letters = count_letters(text)
    letters = counted_letters_to_list(num_letters)
    print("---Begin---")
    print("The book has {} words".format(num_words))
    print()
    for letter in letters:
        print("The letter {} appears {} times".format(letter, num_letters[letter]))
    print("---End---")
    
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}

    for letter in text:
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def counted_letters_to_list(counted_letters):
    letters_lower = []
    for letter in counted_letters:
        if letter.isalpha():
            letters_lower.append(letter)
    return letters_lower


def read_book(path):
    with open(path) as f:
        return f.read()
    

main()