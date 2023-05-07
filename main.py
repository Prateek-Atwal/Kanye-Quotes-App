from tkinter import *
import requests
quote = ""


def get_quote():
    global quote
    res = requests.get(url="https://api.kanye.rest/")
    res.raise_for_status()
    print(f"Status code {res.status_code}")
    return res.json()["quote"]


def new_quote():
    global quote
    quote = get_quote()
    canvas.itemconfig(quote_label, text=quote)


quote = get_quote()
window = Tk()
window.title("Kanye Quotes")
window.config(padx=40, pady=50)

background_img = PhotoImage(file="./background.png")
kanye_img = PhotoImage(file="./kanye.png")

canvas = Canvas(width=300, height=414)
canvas.create_image(150, 207, image=background_img)
quote_label = canvas.create_text(150, 207, text=quote, font=("Arial", 16, "normal"), width=250)
canvas.grid(row=0, column=0)

button = Button(image=kanye_img, command=new_quote)
button.grid(row=1, column=0)

window.mainloop()
