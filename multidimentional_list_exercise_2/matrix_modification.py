num = int(input())
matrix = []

for _ in range(num):
    data = [int(el) for el in input().split()]
    matrix.append(data)

command = input().split()

while command[0] != "END":
    current_command, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])
    if not (0 <= row < num and 0 <= col <= num):
        print("Invalid coordinates")

    elif current_command == "Add":
        matrix[row][col] += value

    elif current_command == "Subtract":
        matrix[row][col] -= value

    command = input().split()

for element in matrix:
    print(*element)