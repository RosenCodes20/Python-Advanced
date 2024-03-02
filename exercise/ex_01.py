n = int(input())
matrix = []

for _ in range(1, n + 1):
    rows = []
    for _ in range(n):
        rows.append(i)
    matrix.append(rows)

for element in matrix:
    print(*element, sep=",")