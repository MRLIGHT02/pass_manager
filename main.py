from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genrate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 3))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 3))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSW(ORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_user_name_entry.get()
    password = password_entry.get()
    pyperclip.copy(email)
    pyperclip.copy(website)

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password) <= 2 or len(email) < 5:
        messagebox.showerror(title="Erorr Massage", message="Please write valid info")



    else:
        messagebox.askokcancel(title=website,
                               message=f"There are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        try:
            with open("./data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("./data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("./data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            website_input.delete(0, END)
            password_entry.delete(0, END)

def search():
    website = website_input.get()
    try:
        with open("./data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message=f"No Data File Found  .")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showerror(title="Error",message=f"No Details for {website} exists. ")

        # http: // wick3dirtyfhcap4y5umkablzkwwrxgpgzg524dgxkiifmh7mgpz4zyd.onion


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0, bg='white')
photo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# TODO CREATING WEBSITE LABLE AND ENTRY WITH THIS USING GRID WITH COLUMNSPAN

website_lable = Label(text="Website:", bg='white', fg='black')
website_lable.grid(column=0, row=1)

website_input = Entry(width=40, bg='white', fg='black')
website_input.focus()

website_input.grid(column=1, row=1)

# TODO CREATING EMAIL/USERNAME LABLE AND ENTRY
email_user_name = Label(text="Email/Username:", bg='white', fg='black')
email_user_name.grid(column=0, row=2)

email_user_name_entry = Entry(width=40, bg='white', fg='black')
email_user_name_entry.insert(END, "name@gamil.com")
email_user_name_entry.grid(column=1, row=2)

# TODO CREATING PASSWORD LABLE AND  ENTRY WITH GENERATE BUTTON

password = Label(text="Password:", bg='white', fg='black')
password.grid(column=0, row=3)

password_entry = Entry(width=40, bg='white', fg='black')
password_entry.insert(0, "1234567")
password_entry.grid(column=1, row=3)

# TODO MAKING BUTTONS GENERATE AND ADD

genrate_button = Button(text="generate password ", bg='white', fg='black', command=genrate_password)
genrate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37, bg='white', fg='black', command=save)
add_button.grid(column=1, row=4, )

search_button = Button(text="Search", bg='white', fg='black', command=search,width=15)
search_button.grid(column=2, row=1)

window.mainloop()
