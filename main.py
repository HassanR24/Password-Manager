from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
from pyperclip import copy
import json
# ----------------------------- SEARCH PASSWORD -------------------------------- #


def find_password():

    website = website_input.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("No Data", "No passwords saved!")
    else:
        if website in data:
            username = data[website]['Username']
            password = data[website]['Password']
            messagebox.showinfo(website, f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showerror("Not Found", f"No data for {website} found!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numb = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numb + password_letter + password_symbol

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_file():
    website = website_input.get().title()
    username = username_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "Username": username,
            "Password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Blank Field", message="Complete data is required.")
        return
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(70, 100, image=bg_image)
canvas.grid(column=1, row=0, columnspan=2)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()
username_input = Entry(width=38)
username_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_file)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
