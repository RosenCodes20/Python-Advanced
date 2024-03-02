from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

text = ""
is_found = False
while vowels and consonants:
    first_vowel = vowels.popleft()
    last_consonant = consonants.pop()

    for flower in flowers.keys():
        flowers[flower] = flowers[flower].replace(first_vowel, "")
        flowers[flower] = flowers[flower].replace(last_consonant, "")

        if flowers[flower] == "":
            print(f"Word found: {flowers[flower]}")
            is_found = True
            break

    if is_found:
        break
