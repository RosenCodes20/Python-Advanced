n = int(input())
matrix = []

for _ in range(n):
    data = [int(el) for el in input().split(", ")]  # data = ['1', '2', '3', '4']; data = [1, 2, 3, 4]
    matrix.append(data)

for element in matrix:
    print(*element, sep=", ")