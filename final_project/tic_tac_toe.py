import speech_recognition as sr

from collections import deque


def get_name(player_number):
    while True:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print(f"Player {player_number} please say your name:")

            audio = r.record(source, duration=3)
            print("Recognizing...")

            try:
                return r.recognize_google(audio)

            except sr.exceptions.UnknownValueError:
                print("Say your name again!")


def get_matrix():
    return [print(f"| {' | '.join(row)} |") for row in tic_toe_board]


SIZE = 3
turns = 0

tic_toe_board = [[str(r + c) for c in range(SIZE)] for r in range(1, SIZE * SIZE + 1, SIZE)]

players = deque()

player_one_name = get_name(1)
player_two_name = get_name(2)

while True:
    player_one_symbol = input(f"{player_one_name} please enter a symbol you would like to play(X or O):").upper()

    if player_one_symbol not in ["X", "O"]:
        print(f"{player_one_name} please select a valid option!")

    else:
        break

player_two_symbol = "O" if player_one_symbol == "X" else "X"

players.append({"name": player_one_name, "symbol": player_one_symbol})
players.append({"name": player_two_name, "symbol": player_two_symbol})

print(f"This is the numeration of the board:")
get_matrix()


def empty_some_matrix_spaces():
    for row in range(SIZE):
        for col in range(SIZE):
            tic_toe_board[row][col] = " "


empty_some_matrix_spaces()
print(f"{players[0]['name']} starts first!")


def main_func():
    turns = 0
    while True:
        try:
            position = int(input(f"{players[0]['name']} please select a position [1-{SIZE * SIZE}]: "))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE

        except ValueError:
            print(f"{players[0]['name']} please enter a valid number!")
            continue

        if 1 <= position <= SIZE * SIZE and tic_toe_board[row][col] == " ":
            turns += 1
            tic_toe_board[row][col] = players[0]['symbol']
            player_name, symbol = players[0].values()
            first_diagonal_win = all([tic_toe_board[i][i] == symbol for i in range(SIZE)])
            second_diagonal_win = all([tic_toe_board[i][SIZE - i - 1] == symbol for i in range(SIZE)])
            row_win = any([all([el == symbol for el in row]) for row in tic_toe_board])
            col_win = any([all([tic_toe_board[col][row] == symbol for col in range(SIZE)]) for row in range(SIZE)])
            get_matrix()

            if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
                print(f"{player_name} won the game!")
                with open("winner.txt", "a") as winner_file:
                    winner_file.write(f"{player_name} won the game!\n")
                raise SystemExit

            if turns == SIZE * SIZE:
                print(f"Draw!")
                raise SystemExit

            players.rotate()

        else:
            print(f"{players[0]['name']} please enter a valid number!")

