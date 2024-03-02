letters = input().split(", ")
letters_dictionary = {}
for letter in letters:
    if letter not in letters_dictionary:
        letters_dictionary[letter] = ord(letter)

print(letters_dictionary)