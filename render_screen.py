from tkinter import Button, Label, Entry
from validations import *
from json import dumps, loads
from shop_main_screen import *
from clear_window import *


def main_screen(tk):
    Button(tk, text="Login", bg="white", fg="black", command=lambda: login(tk)).grid(row=0, column=0)
    Button(tk, text="Register", bg="white", fg="black", command=lambda: register(tk)).grid(row=0, column=1)


def register(tk):
    clear_window(tk)

    Label(tk, text="Email:", font=('calibre', 10, 'bold')).grid(row=0, column=0)
    email_entry = Entry(tk, font=('calibre', 10, 'normal'))
    email_entry.grid(row=0, column=1)

    Label(tk, text="Password:", font=('calibre', 10, 'bold')).grid(row=1, column=0)
    password_entry = Entry(tk, font=('calibre', 10, 'normal'), show="*")
    password_entry.grid(row=1, column=1)

    Label(tk, text="Confirm password:", font=('calibre', 10, 'bold')).grid(row=2, column=0)
    conform_password_entry = Entry(tk, font=('calibre', 10, 'normal'), show="*")
    conform_password_entry.grid(row=2, column=1)

    def valid_registration():
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = conform_password_entry.get()

        with open("./data.db", "r") as file:
            for line in file:
                if email in line:
                    return Label(tk, text="Email already exists!", foreground="red").grid(row=3, column=1)

        if not valid_email(email):
            return Label(tk, text="Invalid email!", foreground="red").grid(row=3, column=1)
        elif not matching_password(password, confirm_password):
            return Label(tk, text="Passwords doesn't match!", foreground="red").grid(row=3, column=1)
        elif not valid_password(password, confirm_password):
            return Label(tk,
                         text="Password must be between 6 and 16 characters!",
                         foreground="red").grid(row=3, column=1)

        data = {"email": email, "password": password, "confirm_password": confirm_password}

        with open("./data.db", "a") as db:
            db.write(f"{dumps(data)}\n")

        Label(tk, text="Successfully registered!", foreground="green").grid(row=3, column=1)

    Button(tk, text="Register", command=lambda: valid_registration()).grid(row=4, column=1)
    Button(tk, text="Back", command=lambda: (clear_window(tk), main_screen(tk))).grid(row=5, column=1)


def login(tk):
    clear_window(tk)

    Label(tk, text="Email:", font=('calibre', 10, 'bold')).grid(row=0, column=0)
    email_entry = Entry(tk, font=('calibre', 10, 'normal'))
    email_entry.grid(row=0, column=1)

    Label(tk, text="Password:", font=('calibre', 10, 'bold')).grid(row=1, column=0)
    password_entry = Entry(tk, font=('calibre', 10, 'normal'), show="*")
    password_entry.grid(row=1, column=1)

    def valid_login():
        email = email_entry.get()
        password = password_entry.get()

        is_found_email = False

        with open("./data.db", "r") as file:
            for line in file:
                if email in line:
                    data = loads(line)
                    if data["email"] == email and data["password"] == password:
                        is_found_email = True
                        clear_window(tk)
                        shop_screen(tk)
                    else:
                        Label(tk, text="Invalid email/password!", foreground="red").grid(row=2, column=1)
                        break

            if not is_found_email:
                Label(tk, text="Invalid email/password!", foreground="red").grid(row=2, column=1)

    Button(tk, text="Log in", command=lambda: valid_login()).grid(row=3, column=1)
    Button(tk, text="Back", command=lambda: (clear_window(tk), main_screen(tk))).grid(row=4, column=1)
