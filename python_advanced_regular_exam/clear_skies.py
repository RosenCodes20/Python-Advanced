rows = int(input())

matrix = [list(input()) for _ in range(rows)]
armor = 300
positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}
jetfighter_pos = []
enemy_count = 0
for row in range(rows):

    if "J" in matrix[row]:
        jetfighter_pos = [row, matrix[row].index("J")]
        matrix[jetfighter_pos[0]][jetfighter_pos[1]] = "-"

    enemy_count += matrix[row].count("E")

command = input()
while enemy_count > 0:
    jetfighter_pos = [jetfighter_pos[0] + positions[command][0], jetfighter_pos[1] + positions[command][1]]
    current_pos = matrix[jetfighter_pos[0]][jetfighter_pos[1]]
    matrix[jetfighter_pos[0]][jetfighter_pos[1]] = "-"

    if current_pos == "E":
        enemy_count -= 1
        if enemy_count <= 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        else:
            armor -= 100

    elif current_pos == "R":
        armor = 300

    if armor <= 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jetfighter_pos[0]}, {jetfighter_pos[1]}]!")
        break

    command = input()

matrix[jetfighter_pos[0]][jetfighter_pos[1]] = "J"

[print("".join(row)) for row in matrix]