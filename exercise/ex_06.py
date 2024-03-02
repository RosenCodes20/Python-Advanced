rows, cols = [int(el) for el in input().split(", ")]
matrix = [] # [[1, 3, 5, 1]]

for _ in range(rows):
    data = list(input().split(", "))
    matrix.append(data)

element_to_search = input()
is_found = False
for rows_index in range(rows): # rows_index = 0
    for cols_index in range(cols):
        if matrix[rows_index][cols_index] == element_to_search:
            print(f"{rows_index}, {cols_index}")
            is_found = True

if not is_found:
    print("Element not in matrix!")