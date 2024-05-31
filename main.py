from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def generate_password():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','&','*','(',')',"+"]

    password_letters = [choice(letters) for char in range(randint(0, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(0, 4))]
    password_number = [choice(numbers) for ch in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_number
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_web = web_input.get()
    new_email = email_input.get()
    new_pass = pass_input.get()
    new_data = {
        new_web: {
            'email': new_email,
            'password': new_pass
        }
    }

    if len(new_web) == 0 or len(new_pass) == 0:
        messagebox.askokcancel(title="Validation", message="Please make sure you haven't left any fields empty.\Input field invalid")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with mew data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)



def find_password():
    old_input = web_input.get()
    try:
        with open("data.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Key not found")
    else:
        if old_input in data:
            new_email = data[old_input]["email"]
            new_pass = data[old_input]["password"]
            messagebox.showinfo(title=old_input, message=f"Name:{old_input}\nEmail:{new_email}\nPassword:{new_pass}",)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {old_input} found")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width=200)
mypass_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_pic)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

web_input = Entry()
web_input.grid(row=1, column=1)
web_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "example@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

pass_input = Entry(width=21)
pass_input.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4,column=1, columnspan=2)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)




window.mainloop()