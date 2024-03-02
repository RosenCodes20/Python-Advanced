n = int(input())
matrix = [list(input()) for _ in range(n)]

entering_game_amount = 100
gambler_position = []
positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}

for rows in range(n):
    if "G" in matrix[rows]:
        gambler_position = [rows, matrix[rows].index("G")]
        matrix[gambler_position[0]][gambler_position[1]] = "-"


turn = input()

while turn != "end":
    gambler_position = [positions[turn][0] + gambler_position[0], positions[turn][1] + gambler_position[1]]
    current_char = matrix[gambler_position[0]][gambler_position[1]]
    matrix[gambler_position[0]][gambler_position[1]] = "-"

    if current_char == "W":
        entering_game_amount += 100

    elif current_char == "P":
        entering_game_amount -= 200

    elif current_char == "J":
        print(f"You win the Jackpot!")
        entering_game_amount += 100_000
        matrix[gambler_position[0]][gambler_position[1]] = "G"
        break

    if not (0 <= gambler_position[0] < n and 0 <= gambler_position[1] < n) or entering_game_amount <= 0:
        print("Game over! You lost everything!")
        break

    turn = input()

matrix[gambler_position[0]][gambler_position[1]] = "G"

if entering_game_amount > 0:
    print(f"End of the game. Total amount: {entering_game_amount}$")
    for row in matrix:
        print(''.join(map(str, row)))
        