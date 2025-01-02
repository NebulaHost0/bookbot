def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        contents_lower = file_contents.lower()
        characters = {}
        for letter in contents_lower:
            characters[letter] = characters.get(letter, 0) + 1
            

    
main()