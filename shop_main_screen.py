from json import loads
from tkinter import *
from PIL import ImageTk, Image
from clear_window import *


def add_image(tk, row, col, path):
    img = Image.open(f"./images/{path}")
    img = img.resize((50, 50), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(tk, image=img)
    panel.image = img
    panel.grid(row=row, column=col)


def shop_screen(tk):
    with open("./data_images", "r") as file_img:
        row = 0
        col = 0
        current_row = 0
        for line in file_img:
            data = loads(line)
            product = data["product"]
            path = data["image_path"]
            quantity = data["quantity"]
            product_id = data["id"]

            Label(tk, text=product).grid(row=row, column=col)
            row += 1

            add_image(tk, row, col, path)
            row += 1

            Label(tk, text=product_id).grid(row=row, column=col)
            row += 1

            Button(tk, text=f"Buy {quantity}", command=lambda: clear_window(tk)).grid(row=row, column=col)

            if col == 5:
                row += 2
                current_row = row
                col = 0
            else:
                col += 1
                row = current_row


