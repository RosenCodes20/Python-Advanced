rows, cols = 6, 6
matrix = [input().split() for _ in range(rows)]

positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}
rover_pos = []
water = 0
concrete = 0
metal = 0
for row in range(rows):
    if "E" in matrix[row]:
        rover_pos = [row, matrix[row].index("E")]

commands = input().split(", ")

for command in commands:
    rover_pos = [(rover_pos[0] + positions[command][0]) % rows, (rover_pos[1] + positions[command][1]) % cols]

    current_pos = matrix[rover_pos[0]][rover_pos[1]]
    if current_pos == "W":
        water += 1
        print(f"Water deposit found at ({rover_pos[0]}, {rover_pos[1]})")

    elif current_pos == "M":
        metal += 1
        print(f"Metal deposit found at ({rover_pos[0]}, {rover_pos[1]})")

    elif current_pos == "C":
        concrete += 1
        print(f"Concrete deposit found at ({rover_pos[0]}, {rover_pos[1]})")

    elif current_pos == "R":
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

if water > 0 and metal > 0 and concrete > 0:
    print("Area suitable to start the colony.")

else:
    print("Area not suitable to start the colony.")