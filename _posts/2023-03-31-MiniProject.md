---
title: "Mini Project - Notes and Todo Manager"
date: 2023-03-31
---

After learning for six weeks and a short break, it's time for a mini project. We were asked to scope the project such that it is not a lot of work for the limited time available and we did just that.

We developed Notes and Todos manager application as part of the project using the tkinter library in python.

Here are the features 

- **Notes**:
  - Add quick and short notes.  
  - View, Modify and delete notes
- **Todos**:
  - Add items to the to-do list
  - View, Modify and delete items from the to-do list
  - Add a due date to the to-do item


<code>from django.contrib.auth</code>
<a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week5\firstWebapplicationWithDjango/authentication/templates/authentication/signup.html">HTML page</a> 
```python
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!")
```

