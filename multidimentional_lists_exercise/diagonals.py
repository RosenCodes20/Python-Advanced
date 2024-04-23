rows = int(input())
matrix = []

for i in range(rows):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)

primary_diagonal = 0
secondary_diagonal = 0
primary_diagonal_elements = []
secondary_diagonal_elements = []
for rows_index in range(rows):
    primary_diagonal += matrix[rows_index][rows_index]
    secondary_diagonal += matrix[rows_index][rows - rows_index - 1]
    primary_diagonal_elements.append(matrix[rows_index][rows_index])
    secondary_diagonal_elements.append(matrix[rows_index][rows - rows_index - 1])

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal_elements))}. Sum: {primary_diagonal}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal_elements))}. Sum: {secondary_diagonal}")

