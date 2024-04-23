some_string = input()

letters_dict = {}

for letter in some_string:
    if letter not in letters_dict:
        letters_dict[letter] = 1

    elif letter in letters_dict:
        letters_dict[letter] += 1

is_valid_string = False
for letter, times in letters_dict.items():
    if times > 1:
        if times - 1 == 1:
            is_valid_string = True

        else:
            is_valid_string = False

if is_valid_string:
    print("YES")

else:
    print("NO")