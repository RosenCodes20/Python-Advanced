def search_numbers(num_as_string: str):
    try:
        num = int(input())
        numbers_dictionary[num_as_string] = num

    except ValueError:
        print("Sorry, the value must be an integer!")


def remove(searched_num):
    try:
        print(numbers_dictionary[searched_num])

    except KeyError:
        print("The given number does not exists in the dictionary!")


def end(element_to_search):
    try:
        del numbers_dictionary[element_to_search]

    except KeyError:
        print("The given number does not exists in the dictionary!")


numbers_dictionary = {}

search_lines = input()

while search_lines != "Search":
    number_as_string = search_lines
    search_numbers(number_as_string)
    search_lines = input()

remove_lines = input()

while remove_lines != "Remove":
    searched = remove_lines
    remove(searched)
    remove_lines = input()

end_lines = input()

while end_lines != "End":
    searched = end_lines
    end(searched)
    end_lines = input()

print(numbers_dictionary)
