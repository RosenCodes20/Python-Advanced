n = int(input())
matrix = []
total_sum = 0

for i in range(n):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)

for lst in matrix:
    total_sum += sum(lst)

print(total_sum)