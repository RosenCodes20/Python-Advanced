import sys

rows, cols = [int(el) for el in input().split()]

matrix = []

for i in range(rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)

sum_of_elements = 0
max_num = -sys.maxsize
final_matrix = []
for row_index in range(rows - 2):
    for cols_index in range(cols - 2):
        first_row_element = matrix[row_index][cols_index]
        first_row_second_el = matrix[row_index][cols_index + 1]
        first_row_third_el = matrix[row_index][cols_index + 2]
        second_row_element = matrix[row_index + 1][cols_index]
        second_row_second_el = matrix[row_index + 1][cols_index + 1]
        second_row_third_el = matrix[row_index + 1][cols_index + 2]
        third_row_element = matrix[row_index + 2][cols_index]
        third_row_second_el = matrix[row_index + 2][cols_index + 1]
        third_row_third_el = matrix[row_index + 2][cols_index + 2]

        sum_of_elements = first_row_element + first_row_second_el + first_row_third_el \
                          + second_row_element + second_row_second_el + second_row_third_el \
                          + third_row_element + third_row_second_el + third_row_third_el

        if sum_of_elements > max_num:
            max_num = sum_of_elements
            final_matrix = [[first_row_element, first_row_second_el, first_row_third_el],
                            [second_row_element, second_row_second_el, second_row_third_el],
                            [third_row_element, third_row_second_el, third_row_third_el]
                            ]

print(f"Sum = {max_num}")
for elements in final_matrix:
    print(*elements)
