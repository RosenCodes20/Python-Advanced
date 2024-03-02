from collections import deque

textiles = deque(int(el) for el in input().split())
medicaments = deque(int(el) for el in input().split())
items = {"Bandage": 0, "MedKit": 0, "Patch": 0}
while textiles and medicaments:
    current_textil = textiles.popleft()
    current_medicament = medicaments.pop()

    sum_of_elements = current_textil + current_medicament
    if sum_of_elements == 30:
        items["Patch"] += 1

    elif sum_of_elements == 40:
        items["Bandage"] += 1

    elif sum_of_elements == 100:
        items["MedKit"] += 1

    elif sum_of_elements > 100:
        items["MedKit"] += 1
        sum_of_elements -= 100
        medicaments[-1] += sum_of_elements

    else:
        current_medicament += 10
        medicaments.append(current_medicament)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")

elif not medicaments:
    print("Medicaments are empty.")

for element, value in sorted(items.items(), key=lambda x:(-x[1], x[0])):
    if value > 0:
        print(f"{element} - {value}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")