rows = int(input())
matrix = []

for i in range(rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)

primary_diagonal = 0
secondary_diagonal = 0
for rows_index in range(rows):
    primary_diagonal += matrix[rows_index][rows_index]
    secondary_diagonal += matrix[rows_index][rows - rows_index - 1]

print(abs(primary_diagonal - secondary_diagonal))