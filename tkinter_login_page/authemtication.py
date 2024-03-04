from json import dump, loads
from tkinter import Button, Label, CENTER
from tkinter import Entry
from PIL import ImageTk, Image
from canvas_load import frame, root


def get_name():
    users = []
    with open("user_information.txt", "r") as users_file:
        for line in users_file:
            users.append(loads(line))

    return users


def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        bd=0,
        width=8,
        height=3,
        command=register
    )

    login_button = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        bd=0,
        width=8,
        height=3,
        command=login
    )

    frame.create_window(330, 256, window=register_button)
    frame.create_window(400, 256, window=login_button)
    frame.create_text(355, 200, text="Welcome to my login page", fill="white")
    frame.create_text(560, 560, text="Made by: Rosen Ivanov", fill="blue")


def clean_screen():
    frame.delete("all")


def register():
    clean_screen()

    frame.create_text(275, 200, text="First name:")
    frame.create_text(275, 225, text="Last name:")
    frame.create_text(275, 250, text="Username:")
    frame.create_text(275, 275, text="Password:")

    frame.create_window(375, 200, window=first_name_box)
    frame.create_window(375, 225, window=last_name_box)
    frame.create_window(375, 250, window=username)
    frame.create_window(375, 275, window=password)

    register_button = Button(
        root,
        text="Register",
        fg="white",
        bg="green",
        width=20,
        height=3,
        command=add_to_dict
    )

    frame.create_window(375, 325, window=register_button)


def add_to_dict():
    registration_dict = {
        "First name": first_name_box.get(),
        "Second name": last_name_box.get(),
        "Username": username.get(),
        "Password": password.get(),
    }

    if check_registration(registration_dict):
        with open("user_information.txt", "a") as users_file:
            dump(registration_dict, users_file)
            users_file.write("\n")
            clean_screen()
            render_entry()


def check_registration(registration_dict):
    frame.delete("error")

    for key, value in registration_dict.items():
        if not value.strip():
            frame.create_text(
                375,
                375,
                text=f"Please enter something in {key}!",
                fill="red",
                tags="error"
            )
            return False

    users_data = get_name()

    for user in users_data:
        if user["Username"] == registration_dict["Username"]:
            frame.create_text(
                375,
                375,
                text="Username already taken!",
                fill="red",
                tags="error"
            )
            return False

        elif user["Password"] == registration_dict["Password"]:
            frame.create_text(
                375,
                375,
                text="Password already taken!",
                fill="red",
                tags="error"
            )
            return False

        elif user["First name"] == registration_dict["First name"]:
            frame.create_text(
                375,
                375,
                text="First name already taken!",
                fill="red",
                tags="error"
            )
            return False

        elif user["Second name"] == registration_dict["Second name"]:
            frame.create_text(
                375,
                375,
                text="Last name already taken!",
                fill="red",
                tags="error"
            )
            return False

    return True


def login():
    clean_screen()

    frame.create_text(
        275,
        200,
        text="Username: "
    )
    frame.create_text(
        275,
        225,
        text="Password: "
    )

    frame.create_window(375, 200, window=username)
    frame.create_window(375, 225, window=password)
    login_button = Button(
        root,
        text="Login",
        fg="white",
        bg="blue",
        width=20,
        height=3,
        bd=0,
        command=add_login_dict
    )

    frame.create_window(375, 265, window=login_button)

    frame.create_text(
        320,
        330,
        text="Don't have an account?",
        fill="green"
    )

    frame.create_text(
        285,
        345,
        text="Create one:",
        fill="green"
    )
    dont_have_an_account_button = Button(
        root,
        text="Create",
        fg="white",
        bg="green",
        width=8,
        height=1,
        command=no_account
    )

    frame.create_window(351, 355, window=dont_have_an_account_button)


def add_login_dict():
    registration_dict = {
        "Username": username.get(),
        "Password": password.get()
    }

    if check_login(registration_dict):
        frame.create_text(
            375,
            380,
            text="You have successfully logged in!!!!",
            fill="green"
        )

        frame.create_text(
            375,
            410,
            text="Do you want to go to the shop?:",
            fill="blue"
        )

        yes_button = Button(
            root,
            text="Yes",
            fg="white",
            bg="green",
            width=8,
            height=3,
            command=yes_buttons
        )
        frame.create_window(325, 465, window=yes_button)

        no_button = Button(
            root,
            text="No",
            fg="white",
            bg="red",
            width=8,
            height=3,
            command=no_buttons
        )
        frame.create_window(415, 465, window=no_button)


def check_login(login_dict):
    frame.delete("error")

    for key, value in login_dict.items():
        if not value.strip():
            frame.create_text(
                375,
                315,
                text=f"Please enter something in {key}",
                fill="red",
                tags="error"
            )
            return False

    users_data = get_name()

    for user in users_data:
        current_user = user["Username"]
        current_password = user["Password"]

        if current_user == login_dict["Username"] and current_password == login_dict["Password"]:
            return True

    else:
        frame.create_text(
            375,
            315,
            text="Incorrect username or password!",
            fill="red",
            tags="error"
        )
        return False


def yes_buttons():
    clean_screen()

    global iphone_quantity, quantity_text_id, macbook_price, budget_text_id, iphone_price, quantity

    quantity = 10
    macbook_price = 40
    image_path = "images/macbook.jpg"
    iphone_price = 80
    iphone_quantity = 10

    global img
    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)

    frame.create_image(120, 185, image=img)

    macbook_button = Button(
        root,
        fg="white",
        bg="blue",
        text="Buy Macbook Air",
        width=20,
        height=3,
        command=buy_macbook
    )

    frame.create_window(120, 356, window=macbook_button)

    quantity_text_id = frame.create_text(
        120,
        310,
        text=f"Quantity: {quantity}",
        fill="blue"
    )

    frame.create_text(
        120,
        400,
        text=f"MacBook price: {macbook_price}",
        fill="blue"
    )

    frame.create_text(
        300,
        50,
        text="Here is the shop:",
        fill="blue",
    )

    frame.create_text(
        275,
        450,
        text="Enter your budget:",
        fill="blue"
    )

    frame.create_window(
        388,
        450,
        window=budget
    )

    budget_button = Button(
        root,
        fg="white",
        bg="green",
        text="Enter budget",
        width=20,
        height=3,
        command=budget_display
    )

    frame.create_window(388, 500, window=budget_button)

    global iphone_image, iphone_quantity_text_id

    iphone_image_path = "images/iphone 15 pro.jpg"
    iphone_image = Image.open(iphone_image_path)
    iphone_image = ImageTk.PhotoImage(iphone_image)

    frame.create_image(
        400,
        180,
        image=iphone_image
    )

    iphone_quantity_text_id = frame.create_text(
        400,
        305,
        text=f"Quantity: {iphone_quantity}",
        fill="blue"
    )

    iphone_buy_button = Button(
        root,
        fg="white",
        bg="blue",
        text="Buy an Iphone 15 Pro",
        width=20,
        height=3,
        command=buy_iphone
    )
    frame.create_window(400, 355, window=iphone_buy_button)

    frame.create_text(
        400,
        390,
        text=f"Price: {iphone_price}",
        fill="blue"
    )


def no_buttons():
    clean_screen()
    render_entry()


def no_account():
    register()


def budget_display():
    global budget_text_id, current_budget
    current_budget = int(budget.get())
    budget_text_id = frame.create_text(
        500,
        50,
        text=f"Your budget is: {budget.get()}",
        fill="blue"
    )


def buy_macbook():
    global quantity, quantity_text_id, macbook_price, budget_text_id, current_budget

    if quantity > 0:
        quantity -= 1
        frame.delete(quantity_text_id)
        quantity_text_id = frame.create_text(
            120,
            310,
            text=f"Quantity: {quantity}",
            fill="blue"
        )

    else:
        raise SystemExit

    if current_budget > 0:
        current_budget -= macbook_price
        frame.delete(budget_text_id)

        budget_text_id = frame.create_text(
            500,
            50,
            text=f"Your budget is: {current_budget}",
            fill="blue"
        )

        budget.delete(0, 'end')
        budget.insert(0, str(current_budget))

    else:
        raise SystemExit


def buy_iphone():
    global iphone_quantity, iphone_quantity_text_id, iphone_price, budget_text_id, current_budget

    if iphone_quantity > 0:
        iphone_quantity -= 1
        frame.delete(iphone_quantity_text_id)

        iphone_quantity_text_id = frame.create_text(
            400,
            305,
            text=f"Quantity: {iphone_quantity}",
            fill="blue"
        )

    else:
        raise SystemExit

    if current_budget > 0:

        current_budget -= iphone_price
        frame.delete(budget_text_id)

        budget_text_id = frame.create_text(
            500,
            50,
            text=f"Your budget is: {current_budget}",
            fill="blue"
        )

    else:
        raise SystemExit


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username = Entry(root, bd=0)
password = Entry(root, bd=0, show="*")
budget = Entry(root, bd=0)
