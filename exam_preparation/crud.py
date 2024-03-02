ROWS, COLS = 6, 6

matrix = [input().split() for _ in range(ROWS)]
positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}

start_position = tuple(map(int, input()[1:-1].split(', ')))
my_position = [start_position[0], start_position[1]]

command = input().split(", ")
while command[0] != "Stop":

    if command[0] == "Create":
        direction, value = command[1], command[2]
        my_position = [my_position[0] + positions[direction][0], my_position[1] + positions[direction][1]]

        if matrix[my_position[0]][my_position[1]] == ".":
            matrix[my_position[0]][my_position[1]] = value

    elif command[0] == "Update":
        direction, value = command[1], command[2]
        my_position = [my_position[0] + positions[direction][0], my_position[1] + positions[direction][1]]

        if matrix[my_position[0]][my_position[1]] != ".":
            matrix[my_position[0]][my_position[1]] = value

    elif command[0] == "Read":
        direction = command[1]
        my_position = [my_position[0] + positions[direction][0], my_position[1] + positions[direction][1]]

        if matrix[my_position[0]][my_position[1]] != ".":
            print(matrix[my_position[0]][my_position[1]])

    elif command[0] == "Delete":
        direction = command[1]
        my_position = [my_position[0] + positions[direction][0], my_position[1] + positions[direction][1]]

        if matrix[my_position[0]][my_position[1]] != ".":
            matrix[my_position[0]][my_position[1]] = "."

    command = input().split(", ")

[print(*row) for row in matrix]