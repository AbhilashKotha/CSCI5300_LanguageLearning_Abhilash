import tkinter as tk
import re

def validate_password(password):
    if len(password) < 8:
        return False, "password length is min 8 characters"
    if not re.search("[a-zA-Z]", password):
        return False, "minimum of one alphabet in password."
    if not re.search("[0-9]", password):
        return False, "minimum of one number in password"
    if not re.search("[!@#$%^&*()_+]", password):
        return False, "minimum of one special character in password."
    return True, ""

def validate_username(username):
    if not re.match("^[a-zA-Z]*$", username):
        return False, "username - only alphabets allowed."
    return True, ""

def submit_form():
    username = username_entry.get()
    password = password_entry.get()

    password_valid, password_error = validate_password(password)
    username_valid, username_error = validate_username(username)

    if password_valid and username_valid:
        with open("users.txt", "a") as f:
            f.write(f"Username: {username}\nPassword: {password}\n\n")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        status_label.config(text="User created successfully!")
    else:
        status_label.config(text=password_error + "\n" + username_error)

root = tk.Tk()
root.title("Signup Form")
root.geometry("400x200")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

def show_password():
    password_entry.config(show="")
    show_password_button.config(text="👁️", command=hide_password)

def hide_password():
    password_entry.config(show="*")
    show_password_button.config(text="👁️", command=show_password)

show_password_button = tk.Button(root, text="👁️", command=show_password)
show_password_button.pack()

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
