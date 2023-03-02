---
title: "Fifth week - Web Development with Django"
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
