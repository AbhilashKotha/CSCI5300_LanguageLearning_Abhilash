---
title: "Third week - Getting Real!"
date: 2023-02-15
---

Last two weeks were for basics and concepts. This week I wanted to try and build something near to real world. I went with a desktop application. I know these are not common these days but seeing some working software gives me motivation to learn. 

I searched the internet to find the suitable library to build a windows application. I learnt that there are multiple options like tkinter, PyQT (the one shown in the class for neurons project), wxPython. I selected tkinter, no specific reason though.

I started with a small code, to print <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week3/helloWorld.py">hello world</a> message to the window and then a quit button to kill the instance.

```python
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello_label = tk.Label(self, text="Hello, world!")
        self.hello_label.pack(side="top")
        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

```

But this is very basic. I wanted to get more practical and build a signup page which takes  signup information from the user and saves it to a file. Then, I started building the application and built it successfully, though the UI is not beauitiful(will take care of the UI next time!).

I first designed a small window and wanted to place it at the center of the screen. This is what I did.

```python
root.title("Signup Form")
root.geometry("400x200")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))
```

Now that I have the base, what fields are important for a signup? I thought user name and password are enough for now. So I added those input fileds along with the labels and a submit button. I was smart enough to figure out that I have to hide the password as the user inputs their passowrd.

```python
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
```

Once the user enters the details and clicks on the submit, I have added a method to save the details in a file.

```python
        with open("users.txt", "a") as f:
            f.write(f"Username: {username}\nPassword: {password}\n\n")
```

But is that enough? What if the user enters a password that is not strong and what if the user does not enter anything and just submits it? To answer these questions, I have added multiple validations which are done after the submit button is pressed.

```python

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
```

Now that we have evrything ready for the users to signup, I wanted to make it little more friendly for the users. To add a button to show the password they typed. I was unsuccessful in finding an icon with a closed eye. I only found an open eye which I used for toggling show/hide password. 

While thinking what else could make it easy for the user, I thought how difficult it is to the user to generate a password that meets all the expectations and also strong. I wanted to give a button for the user to generate a password randomly which is strong. This is where the challenge comes. Now, I already have some conditions for my password validations, how do I generate a password which satisfies all those conditions? I used random method to generate a password of legth 12 from all alphabets, digits and special characters but the problem was that it was not taking the "at least 1 from each" condition.I then figured out gow to resolve the issue and finally was able to create a password that matches all the conditions. 

```python
def generate_password():
    length = 4
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    password = "".join((random.choice(letters)+ random.choice(digits) + random.choice(special_chars)) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
```

After clearing all the challenges with random string generation, regular expressions and button placements, I was able to create a good desktop application for signup that looks like below <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week3/windowsApp.py">(link to full code)</a>.

![image](https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week3/imageapp.png)

Though this is a working application, I am not quite satisified with the control that I have on the UI, sometime in next few weeks I want to explore more on the better UI options for python desktop applications. 

This is a good learning for this week and I will continue to build on top of this to dig deeper into these libraries.