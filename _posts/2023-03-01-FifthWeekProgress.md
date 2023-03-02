---
title: "Fourth week - Web Development with Django"
date: 2023-03-01
---
My First Month of learning python was just small to medium programs with just a single file. I decided I must take up complex tasks and asked the professor if I switch to Python Web development and she said it is okay.  This is the first time I am doing web development in python. I chose Django for the same. Below is what my directory tree looks like. 
 

I have started leaning python with the help of two Youtube videos that I found interesting and helpful. Below are their links.

https://www.youtube.com/watch?v=zuxzE7--RYM 
https://www.youtube.com/watch?v=1UvTNMH7zDo 


These videos were instrumental in helping me understand the basic concepts of Django and build my first web application. The First tutorial provided a solid foundation of Django concepts, such as views, templates, settings, and URLs. I have created my first project and an app to display a small HTML page. 


As I started building my web application, I ran into a few challenges. One of the main challenges I faced was figuring out how to add references to multiple places, such as URLs and settings.py (I have listed below some of the snippets from my code). However, with the help of online resources such as Stack Overflow the Django documentation, I was able to overcome these challenges. What I did not understand was, python is so advanced, is it not possible to detect some folders without adding the reference to it? (Maybe there is a different way! I will try to figure it out)
```python
INSTALLED_APPS = [
    'firstAttempt.apps.FirstattemptConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["authentication/templates"],
        'APP_DIRS': True,
        'OPTIONS': {}
}
]
```

```python
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.signout,name='logout'),
]

```

One of the first things I learned was how to create a simple "Hello World" page using Django. I then moved on to building more complex pages with the help of views, templates, and URLs. These concepts were key in helping me structure my web application and make it more organized.

Another important concept I learned was Django commands. These commands allowed me to create new Django applications, run the server, and migrate my database. By understanding these commands, I was able to become more efficient in my development process. I listed some of them below

```bash
python manage.py runserver
python manage.py clearcache
python manage.py shell
python manage.py startapp authentication
django-admin startproject firstWebapplicationWithDjango
```

With the help of the second video, I started writing authentication and authorization code. This is a more complex topic that requires a deeper understanding of Django's built-in authentication and authorization system with the libraries. Although I am still in the process of learning and completing this part of the tutorial, I am excited to see how I can incorporate this functionality into my web application.

image

Overall, my journey learning web development with Django has been exciting and challenging. With the help of the two videos and online resources, I was able to gain a solid understanding of the core concepts of Django and build my first web application. I hope to complete this by next week and add some more functionalities to the application.





/////////////////////////////////////////////////////////////////////////////
It has been a month since I am learning python and I feel that there is no stop to learning with the kind of libraries that Python supports. I realized that it is an ocean.

As I wrote in my last week’s blog, I continued building on top of the application that I created. As I had the signup functionality working, the next step was to allow the users to sign in using their username and password. 
Just to recall, once the user enters the details, I stored them in a text file called "users.txt" when they sign up. The file contained the username and password of each user, separated by a colon. 

![image](https://user-images.githubusercontent.com/113061137/220812626-71efd9b0-1ebf-4b52-ba87-28d142c0c7f7.png)

Instead of creating a separate window for sign-in, I have just created a new button that does the job. Why? Because the signup and sign-in are just based on two fields. Once an existing user enters their details and clicks on the sign-in button, the application checks if the details entered by the user are correct or not against the ones stored in the "users.txt" file. Below is the code that validates the users against the database. This is where the challenge was this time. I know how to read the file and I know how to break a string on a delimiter. But I had difficulty mapping the passwords with respective usernames. This is what I wrote in the beginning. This code lets user sign in with any username and password combination from the database.

```Python
def submit_sign_in_form():
    username = username_entry.get()
    password = password_entry.get()

    # retrieve usernames and passwords from the file
    with open("users.txt", "r") as f:
        users = f.read().split("\n\n")
    usernames = [user.split("\n")[0].replace("Username: ", "") for user in users]
    passwords = [user.split("\n")[1].replace("Password: ", "") for user in users]

    if username in usernames and password in passwords:
        status_label.config(text="Login successful!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        root.withdraw()
        show_memo_window()
        return
    else:
        status_label.config(text="Invalid username or password.")
```
That is where the dictionaries came to my rescue. I have updated my validation function and the <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week3/helloWorld.py">code</a> looks like below.

```Python
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

```
After the user is successfully authenticated, I wanted to provide them with a new window where they could write a memo for the day. I used the Tkinter library to create a text input field where the user could write anything they want. I also added a "Save" button that would save the memo to a new text file with today's date as the filename.
The screen looks like below,

![image](https://user-images.githubusercontent.com/113061137/220812657-93a4b549-a23f-46e4-ba33-3382ce50cc54.png)

While implementing the memo-saving feature, I learned a new thing called the nested function in Python. A nested function is a function that is defined inside another function and can only be accessed from within that function (just for the scope of the parent function). I created a nested function that saves the file to a local directory.

![image](https://user-images.githubusercontent.com/113061137/220812694-97c3e6a6-86b7-46a6-96ab-df6467ee7f8c.png)

Now that I have the option to save memos, I want the users to be able to view their memos as well. I will continue building features on this if there are still some good learnings, otherwise, I will try for a new library next week. 
