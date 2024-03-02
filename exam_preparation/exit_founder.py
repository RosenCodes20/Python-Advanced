names = input().split(", ")
player = ""
loser = ""
rows, cols = 6, 6

matrix = [input().split() for _ in range(rows)]
tom_wall = False
jerry_wall = False
count = 0
while True:
    command = tuple(map(int, input()[1:-1].split(", ")))
    position = matrix[command[0]][command[1]]

    if count == 2:
        count = 0

    if tom_wall and count == names.index("Tom"):
        count += 1
        tom_wall = False
        continue

    if jerry_wall and count == names.index("Jerry"):
        count += 1
        jerry_wall = False
        continue

    if position == "W" and count == names.index("Tom"):
        player = "Tom"
        tom_wall = True
        print(f"{player} hits a wall and needs to rest.")

    elif position == "W" and count == names.index("Jerry"):
        player = "Jerry"
        jerry_wall = True
        print(f"{player} hits a wall and needs to rest.")

    if position == "T" and count == names.index("Tom"):
        player = "Tom"
        loser = "Jerry"
        print(f"{player} is out of the game! The winner is {loser}.")
        break

    elif position == "T" and count == names.index("Jerry"):
        player = "Jerry"
        loser = "Tom"
        print(f"{player} is out of the game! The winner is {loser}.")
        break

    if position == "E" and count == names.index("Tom"):
        player = "Tom"
        loser = "Jerry"
        print(f"{player} found the Exit and wins the game!" )
        break

    elif position == "E" and count == names.index("Jerry"):
        player = "Jerry"
        loser = "Tom"
        print(f"{player} found the Exit and wins the game!" )
        break
    count += 1

