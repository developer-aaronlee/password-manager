from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list += [random.choice(letters) for x in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list += [random.choice(symbols) for x in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list += [random.choice(numbers) for x in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    # print(f"Your password is: {password}")

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) < 11 or len(password) < 6:
        messagebox.showerror(title=website, message="Please don't leave any field empty")
    else:
        try:
            with open("data.json") as file:
                content = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            content.update(new_data)
            with open("data.json", "w") as file:
                json.dump(content, file, indent=4)
        finally:
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            username_entry.insert(0, "@gmail.com")

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json") as file:
            data = json.load(file)
            username_found = data[website]["username"]
            password_found = data[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for website exists.")
    else:
        messagebox.showinfo(title=website, message=f"un: {username_found}\npw: {password_found}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

search_button = Button(width=13, text="Search", command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
