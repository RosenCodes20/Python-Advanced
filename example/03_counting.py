element_count = input().split(": ")
elements_dict = {} # {ivcho: 5} items = (ivcho, 5) element = ivcho quantity = 5
quantity_of_the_items = 0
while element_count[0] != "START":
    for i in range(0, len(element_count), 2):
        key = element_count[i]
        value = element_count[i + 1]
        if key not in elements_dict:
            elements_dict[key] = int(value)
        elif key in elements_dict:
            elements_dict[key] += int(value)

    element_count = input().split(": ")

print("Products in stock:")

for element, quantity in elements_dict.items():
    quantity_of_the_items += quantity
    print(f"- {element}: {quantity}")

print(f"Total products: {len(elements_dict)}")
print(f"Total quantity: {quantity_of_the_items}")