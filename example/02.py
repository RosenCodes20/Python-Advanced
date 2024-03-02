element_count = input().split()
products_to_search = input().split() # ['coca cola', 'ivcho']
elements_dict = {}

for i in range(0, len(element_count), 2):
    key = element_count[i]
    value = element_count[i + 1]

    if key not in elements_dict:  # {ivcho: 20, sasho: 10}
        elements_dict[key] = int(value)

for element in products_to_search:
    if element in elements_dict:
        print(f"We have {elements_dict[element]} of {element} left")

    else:
        print(f"Sorry we don't have {element}")