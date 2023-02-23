import datetime
import tkinter as tk
import re
import random
import string

def validate_password(password):
    if len(password) < 8:
        return False, "Password < 8 characters"
    if not re.search("[a-zA-Z]", password):
        return False, "Password has no letters."
    if not re.search("[0-9]", password):
        return False, "Password has no numbers."
    if not re.search("[!@#$%^&*()_+]", password):
        return False, "Password has no special characters."
    return True, ""

def validate_username(username):
    if not re.match("^[a-zA-Z]*$", username):
        return False, "Username can only contain letters."
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

def generate_password():
    length = 4
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    password = "".join((random.choice(letters)+ random.choice(digits) + random.choice(special_chars)) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def submit_sign_in_form():
    username = username_entry.get()
    password = password_entry.get()

    # retrieve usernames and passwords from the file
    with open("users.txt", "r") as f:
        users = f.read().split("\n\n")

    user_dict = {}
    for user in users:
        user_lines = user.split("\n")
        username_from_file = user_lines[0].replace("Username: ", "")
        password_from_file = user_lines[1].replace("Password: ", "")
        user_dict[username_from_file] = password_from_file

    if username in user_dict and password == user_dict[username]:
        status_label.config(text="Login successful!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        root.withdraw()
        show_memo_window()
        return
    else:
        status_label.config(text="Invalid username or password.")

def show_memo_window():
    memo_window = tk.Toplevel()
    memo_window.title("Memo for Today")
    memo_window.geometry("400x400")

    memo_text = tk.Text(memo_window, wrap="word")
    memo_text.pack(fill="both", expand=True)

    def save_memo():
        memo = memo_text.get("1.0", "end-1c")
        today = datetime.date.today()
        filename = today.strftime("%Y-%m-%d") + ".txt"
        with open(filename, "w") as f:
            f.write(memo)

    save_button = tk.Button(memo_window, text="Save", command=save_memo)
    save_button.pack()

    memo_window.mainloop()

root = tk.Tk()
root.title("Signup Form")
root.geometry("400x300")

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
show_password_button.pack(side="top")

generate_password_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_password_button.pack(side="top")

submit_button = tk.Button(root, text="Signup", command=submit_form)
submit_button.pack()

signin_button = tk.Button(root, text="Sign in", command=submit_sign_in_form)
signin_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
