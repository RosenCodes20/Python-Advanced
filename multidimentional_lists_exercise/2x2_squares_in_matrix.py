rows, cols = [int(el) for el in input().split()]
matrix = []

for i in range(rows):
    data = list(input().split())
    matrix.append(data)

found_squares = 0
for rows_index in range(rows - 1):
    for cols_index in range(cols - 1):
        current_element = matrix[rows_index][cols_index]
        down_element = matrix[rows_index + 1][cols_index]
        next_element = matrix[rows_index][cols_index + 1]
        down_right_element = matrix[rows_index + 1][cols_index + 1]

        if current_element == down_element == next_element == down_right_element:
            found_squares += 1

print(found_squares)