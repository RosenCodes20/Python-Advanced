n = int(input())
racing_number = input()

matrix = [input().split() for _ in range(n)]
tracked_car = [0, 0]
kilometers = 0
tunnel = []
positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}
for _ in range(n):
    if "T" in matrix[_]:
        tunnel = [_, matrix[_].index("T")]

finished = False
command = input()
while command != "End":
    tracked_car = [positions[command][0] + tracked_car[0], positions[command][1] + tracked_car[1]]
    current_path = matrix[tracked_car[0]][tracked_car[1]]
    if current_path == "T":
        matrix[tracked_car[0]][tracked_car[1]] = "."
        kilometers += 30
        tracked_car = tunnel
        matrix[tracked_car[0]][tracked_car[1]] = "."

    elif current_path == ".":
        kilometers += 10

    elif current_path == "F":
        print(f"Racing car {racing_number} finished the stage!")
        kilometers += 10
        finished = True
        break

    command = input()

matrix[tracked_car[0]][tracked_car[1]] = "C"
if not finished:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {kilometers} km.")

[print(''.join(row)) for row in matrix]