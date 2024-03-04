import random

from tkinter import Tk, Canvas, Button
from tkinter.ttk import Entry, Label

some_text = None


def create_root():
    root = Tk()

    root.title("Love calculator")

    root.geometry("700x600")

    root.resizable(False, False)

    return root


def create_frame():
    frame = Canvas(root, width=700, height=800, bg="cyan")
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()


def main():
    frame.create_text(350, 50, text="Welcome to my love calculator!", fill="black")

    frame.create_text(250, 150, text="Enter first player name: ", fill="black")
    frame.create_window(375, 150, window=first_name)

    frame.create_text(250, 190, text="Enter second player name: ", fill="black")
    frame.create_window(382, 190, window=second_name)

    generate_love_button = Button(
        root,
        fg="white",
        bg="blue",
        text="Generate love",
        width=20,
        height=3,
        command=generate_love
    )

    frame.create_window(325, 250, window=generate_love_button)


def generate_love():
    global some_text
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    num_one = random.choice(nums)
    num_two = random.choice(nums)

    if some_text:
        frame.delete(some_text)

    some_text = frame.create_text(325, 300, text=f"{first_name.get()} loves {second_name.get()} {num_one}{num_two}%", fill="black")


first_name = Entry(root)
second_name = Entry(root)

if __name__ == "__main__":
    main()
    root.mainloop()
