n = int(input())
matrix = []
primary_sum = 0

for _ in range(n):
    data = list(map(int, input().split(", ")))
    matrix.append(data)

for rows_index in range(n): # n = 3; rows_index = 0, 1, 2
    primary_sum += matrix[rows_index][n - rows_index - 1]

print(primary_sum)