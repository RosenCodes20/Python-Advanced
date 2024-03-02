import sys

rows, cols = [int(el) for el in input().split(", ")]
matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)

max_num = sys.maxsize
final_matrix = []
for rows_index in range(rows - 1):
    for cols_index in range(cols - 1):

        current_element = matrix[rows_index][cols_index]
        down_element = matrix[rows_index + 1][cols_index]
        right_element = matrix[rows_index][cols_index + 1]
        down_right_element = matrix[rows_index + 1][cols_index + 1]

        final_sum = current_element + down_element + right_element + down_right_element
        if final_sum < max_num:
            max_num = final_sum
            final_matrix = [[current_element, right_element], [down_element, down_right_element]]

for element in final_matrix:
    print(*element)

print(max_num)