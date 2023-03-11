---
title: "Sixth week - Authentication and Authorization in Django"
date: 2023-03-10
---

It's been two weeks since I started web development using Django and I can say that it is not so easy. At least in the beginning. So many dependencies here and there. But I think that is why it is so lightweight. For a C# solution built in Visual Studio, the code files take at least a few MBs of disc space whereas the code for Django took only a few 100 KBs of disc space. 

As I mentioned last week, I continued to work with Django to complete the authentication and authorization on the web application. While there are good libraries that can handle authentication and authorization, It's important to select the right one. I used <code>from django.contrib.auth</code> for the job. 
Initially, I started with the home page, which has a sign-in button and a sign-up button if the user is not logged in. Otherwise, the page displays a greeting along with a signout button. By following the instructions from the below video, I implemented the authentication and authorization.

<a href="https://www.youtube.com/watch?v=1UvTNMH7zDo">https://www.youtube.com/watch?v=1UvTNMH7zDo</a>

First step, I started with the implementation of the sign-up functionality. I designed a simple <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week5\firstWebapplicationWithDjango/authentication/templates/authentication/signup.html">HTML page</a> that asks for user information and has a submit button. One great learning here is <code>csrf_token</code> which is a Cross-Site Request Forgery (CSRF) token to a form that is used as a security measure to protect against CSRF attacks, which are a type of attack where an attacker can trick a user into executing unwanted actions on a website, by submitting a form with malicious data. Once the user completes the form, the application calls the function from <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week5\firstWebapplicationWithDjango/authentication/templates/authentication/views.py">views.py</a>.In this function, I took all the parameters passed from the interface into the parameters and used the create_user function of the auth library to create the user.

```python
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!")
```
Once the user is created, the application will redirect the user to the sign-in page for which I wrote a simple HTML page that takes the user's information. After the user clicks on the sign-in button, the application calls the function from views.py to complete the sign-in. The code looks like this: I have used <code>authenticate</code> function to authenticate the user. The application takes the users to the home page once the sign-in is complete.

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
The initial Home, login and signup pages were looking very plain and clumsy. I used some simple CSS styles to make it cleaner. Below are the screenshots of the pages and errors.

![image](https://user-images.githubusercontent.com/113061137/224431744-ff11b5f9-9789-47a8-943a-fc59e57c27a3.png)
![image](https://user-images.githubusercontent.com/113061137/224431773-054fe5cd-92b1-46ea-befa-9b402adb2106.png)
![image](https://user-images.githubusercontent.com/113061137/224431778-f86912a0-c4b4-4668-91da-1f8ce29bffb0.png)
![image](https://user-images.githubusercontent.com/113061137/224431792-f82d345c-3db5-4ae5-9a6e-4157110bf40c.png)
![image](https://user-images.githubusercontent.com/113061137/224431840-972f4a26-2f8f-411d-89c7-412d517f1399.png)
![image](https://user-images.githubusercontent.com/113061137/224431861-a6ff2703-f4a5-4576-b29f-e1e2830e0cc6.png)

Isn't it looking too smooth till this point? But it was not as easy as it sounds here. I had challenges in setting up the migrations, understanding the variables, and as always updating the dependencies in multiple places. One major thing was with <code>APPEND_SLASH</code> parameter in the settings.py file. Apparently, Django redirects URLs that do not end in a slash ("/") to the same URL with a trailing slash. This behavior is controlled by the APPEND_SLASH setting in Django. This took some time to fix. Another thing was with the is_active property in the signup function which is by default set to true and needs to be modified according to our needs. The migration was another frustration, one moment, it works and the next moment it does not work. I had to clear all the migrations and re-run them to ensure that no cache would cause errors. 

```bash
rm -f authentication/migrations/*.py
python manage.py migrate authentication zero
python manage.py makemigrations authentication
python manage.py migrate authentication

```

However, a frustrating week of learning but I have learned some good basics. Next week, I will try to implement email functionality to verify the users. This may need some work with Gmail APIs, but I think that would also be good learning.

