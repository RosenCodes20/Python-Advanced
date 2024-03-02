name_number = input().split()
class_dictionary = {} # {ivcho: 50}

for index in range(0, len(name_number), 2): # 0 2 4 6
    key = name_number[index]
    value = name_number[index + 1]
    if key not in class_dictionary:
        class_dictionary[key] = int(value)

print(class_dictionary)