---
title: "Fifth week - Web Development with Django"
date: 2023-03-01
---
My first month of learning Python consisted of only small to medium-sized programs. They all shared a single file. I decided I needed to take on more complex tasks and asked the professor if I could switch to Python Web development; she said it was fine. This is my first attempt at web development in Python, and I chose Django. My code structure is depicted in the screenshot below. 

![image](https://user-images.githubusercontent.com/113061137/222328579-ced1a035-2fc4-4a69-baca-d23e7accd428.png)


I have started leaning python with the help of two Youtube videos that I found interesting and helpful. Below are their links.

<a href="https://www.youtube.com/watch?v=zuxzE7--RYM">https://www.youtube.com/watch?v=zuxzE7--RYM</a>
<br>
<a href="https://www.youtube.com/watch?v=1UvTNMH7zDo">https://www.youtube.com/watch?v=1UvTNMH7zDo</a>


These videos were instrumental in helping me understand the basic concepts of Django and build my first web application. The First tutorial provided a solid foundation of Django concepts, such as views, templates, settings, and URLs. I have created my first project and an app to display a small HTML page. 

![image](https://user-images.githubusercontent.com/113061137/222328876-b77e44ba-0f52-4376-ba20-c5b6f51e82b9.png)


As I started building my web application, I ran into a few challenges. One of the main challenges I faced was figuring out how to add references to multiple places, such as <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles\week5\firstWebapplicationWithDjango\firstWebapplicationWithDjango\urls.py">urls.py</a> and <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles\week5\firstWebapplicationWithDjango\firstWebapplicationWithDjango\settings.py">settings.py</a> (I have listed below some of the snippets from my code). However, with the help of online resources such as Stack Overflow the Django documentation, I was able to overcome these challenges. What I did not understand was, python is so advanced, is it not possible to detect some folders without adding the reference to it? (Maybe there is a different way! I will try to figure it out)
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

As we all start with a hello world program for everything, I also started with a simple "Hello World" page using Django and python. I then continued to build complex pages with the help of views, templates, and URLs. With the help of these, I learned how to organize different parts of the project in a better way.

Another important concept I learned was Django commands. These commands allowed me to create new Django applications, run the server, and migrate my database. By understanding these commands, I was able to become more efficient in my development process. I listed some of them below

```bash
python manage.py runserver
python manage.py clearcache
python manage.py shell
python manage.py startapp authentication
django-admin startproject firstWebapplicationWithDjango
```

With the help of the second video, I started writing authentication and authorization code. This is a more complex topic that requires a deeper understanding of Django's built-in authentication and authorization system with the libraries. Although I am still in the process of learning and completing this part of the tutorial, I am excited to see how I can incorporate this functionality into my web application.

![image](https://user-images.githubusercontent.com/113061137/222328920-46f7e7ca-6edd-4fc1-a13e-f68bebb669c0.png)

Overall, my journey learning web development with Django has been exciting and challenging. With the help of the two videos and online resources, I was able to gain a solid understanding of the core concepts of Django and build my first web application. I hope to complete this by next week and add some more functionalities to the application.
