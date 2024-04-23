def move(current_position, value):
    rows = my_position[0] + (positions[current_position][0] * value)
    cols = my_position[1] + (positions[current_position][1] * value)
    if not (0 <= rows < SIZE and 0 <= cols < SIZE):
        return my_position
    if matrix[rows][cols] == "x":
        return my_position
    return [rows, cols]


def shoot(position):
    rows = my_position[0] + positions[position][0]
    cols = my_position[1] + positions[position][1]

    while 0 <= rows < SIZE and 0 <= cols < SIZE:
        if matrix[rows][cols] == "x":
            matrix[rows][cols] = "."
            return [rows, cols]

        rows += positions[position][0]
        cols += positions[position][1]


SIZE = 5
matrix = []
my_position = []
targets = 0
positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}
targets_hit_positions = []
targets_hit = 0
for row in range(SIZE):
    data = input().split()
    matrix.append(data)

    if "A" in matrix[row]:
        my_position = [row, matrix[row].index("A")]

    targets += matrix[row].count("x")

for _ in range(int(input())):

    command = input().split()

    if command[0] == "shoot":
        targets_down_hit = shoot(command[1])
        if targets_down_hit:
            targets_hit_positions.append(targets_down_hit)
            targets_hit += 1

        if targets_hit == targets:
            print(f"Training completed! All {targets} targets hit.")
            break

    elif command[0] == "move":
        my_position = move(command[1], int(command[2]))

if targets_hit < targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")

print(*targets_hit_positions, sep="\n")