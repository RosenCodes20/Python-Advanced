name_class = input().split(":")

class_dict = {}
while name_class[0] != "End":
    for index in range(0, len(name_class), 3):
        key = name_class[index]
        class_number = name_class[index + 1]
        class_value = name_class[index + 2]

        if key not in class_dict:
            class_dict[key] = [class_number, class_value]

    name_class = input().split(":")

class_to_search = input()

for name, number_class in class_dict.items():

    if class_to_search in number_class:
        print(f"{name} - {number_class[0]}")