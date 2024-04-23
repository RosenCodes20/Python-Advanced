import re

some_text = input()

lowercase = 0
uppercase = 0
digits = 0
other = 0

lowercase_letters_regex = r"[a-z]"
uppercase_letters_regex = r"[A-Z]"
digits_regex = r"[0-9]"

found_lowercase_letters = re.findall(lowercase_letters_regex, some_text)
found_uppercase_letters = re.findall(uppercase_letters_regex, some_text)
found_digits = re.findall(digits_regex, some_text)

if found_lowercase_letters:
    lowercase += len(found_lowercase_letters)

if found_uppercase_letters:
    uppercase += len(found_uppercase_letters)

if found_digits:
    digits += len(found_digits)

for letter in some_text:
    if not letter.isalpha() and not letter.isdigit():
        other += 1

print(f"Digits count: {digits}")
print(f"Lowercase letters count: {lowercase}")
print(f"Uppercase letters count: {uppercase}")
print(f"Other symbols count: {other}")