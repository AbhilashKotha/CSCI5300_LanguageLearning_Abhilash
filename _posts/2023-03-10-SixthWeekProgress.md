---
title: "Sixth week - Authentication and Authorization in Django"
date: 2023-03-10
---

It's been two weeks since I started web development using Django and I can say that it is not so easy. At least in the beginning. So many dependencies here and there. But I think that is why it is so light weight. For a C# solution built in Visusl studo, the code files take at least few MBs of disc space whereas the code for Django took only few 100 KBs of disc space. 

As I mentioned last week, I continued to work with Django to complete the authentication and authorization on the web application. While there are good libraries that can handle authentication and authorization, It's important to select the right one. I used <code>from django.contrib.auth</code> for the job. 

Initially I started with the home page, which has a sign in button and a sign up button if the user is not logged in. Otherwise, the page displays a greeting along with a signout button. By following the instructions from the below video, I implemented the authentication and authorization.

<a href="https://www.youtube.com/watch?v=1UvTNMH7zDo">https://www.youtube.com/watch?v=1UvTNMH7zDo</a>

First step, I started with the implementation of signup functionality. I designed a simple html page that asks for the user information and has a sumbit button. One great learning here is <code>{% csrf_token %}</code> which is a Cross-Site Request Forgery (CSRF) token to a form that is used as a security measure to protect against CSRF attacks, which are a type of attack where an attacker can trick a user into executing unwanted actions on a website, by submitting a form with malicious data. Once the user completes the form, the application call the function from views.py.In this function I took all the parameters passed from the interface into the parameters and the used the create_user function of the auth library to create the user.

```python
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!")
```
Once the user is created, the application will redirect the use to signin page for which I wrote a simple html page which takes the user information. After user clicks on the signin button, the application calls the function from views.py to complete the signin. The code looks like this: I have used <code>authenticate</code> function to authenticate the user. The application takes the users to home page once the signin is complete.

```python
user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
```
The initial Home, login and signup pages were looking very plain and clumsy. I used some simple CSS styles to make it cleaner.Below are teh screenshots of the pages and errors.



![image](https://user-images.githubusercontent.com/113061137/222328579-ced1a035-2fc4-4a69-baca-d23e7accd428.png)

<a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles\week5\firstWebapplicationWithDjango\firstWebapplicationWithDjango\urls.py">urls.py</a>