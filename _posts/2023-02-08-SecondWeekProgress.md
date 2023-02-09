---
title: "Second week - It gets more challenging"
date: 2023-02-08
---

After the successful first week, I wanted to resume where I left off. I started with a simple exercise to work with <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week2/functions.py">functions</a> and it was a cakewalk.

```python
def draftGreeting(name):
    # drafts greeting for an email after passing a name
    print("Hello, " + name + ",")

nameOfRecipient = input("Who is the recipient: ")
draftGreeting(nameOfRecipient)
```

After this, I have done the following exercises using python:

1.	Using classes
2.	Using dictionaries
3.	Exception handling
4.	working with lists
5.	working with regular expessions

I started working with <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week2/lists.py">lists</a> and it was easy as well. I observed that the list order stays persistent throughout the program in python. Below is the code I wrote.

```python
subjects = ["Software Engineering", "Computing and Society", "Human Computer Interaction"]

print("Here are the list of subjects available for spring semester")
print(subjects)

choice = input("What do you want to do: 1: add a subject 2: remove a subject ")
subName = input("what is the subject?")
if(choice=="1"):
    subjects.append(subName)
    print("subject added")
    print(subjects)
else:
    subjects.remove(subName)
    print("subject removed")
    print(subjects)
```
Then comes the concept of <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week2/dictionaries.py">dictionaries</a> , which was somewhat new to me. While learning this, I had no issues but one challenge was that I was constantly getting an error while iterating through the elements and printing them. That was because of the data type issue. That is when I realized that a single dictionary can store multiple data types. I was under the assumption that all the elements will be of the same type. 
Now I jumped to the concept of classes. Here is what I tried and I was again successful in executing the program without any errors. 

```python
class CollegeEvent:

    def __init__(self, eventTitle, location, date):
        self.eventTitle = eventTitle
        self.location = location
        self.date = date

    def createInvitation(self):
        return "You are invited to " + self.eventTitle + " event which is happening at " + self.location + " on this " + self.date +"th"

CollegeEvent = CollegeEvent("recruitment", "Busch", "17")
print(CollegeEvent.createInvitation()) 
```
Regular expressions are always confusing to me, with so many characters and symbols written together, looks like gibberish. Takes time to understand what each letter is doing. I wrote a program to <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week2/regEx.py">extract email addresses</a> from a given string. The challenge was that my program was picking up all the text has an ‘@’ symbol. That is not what I wanted. I wanted the email to look like something@something.some. I had to add another condition to the pattern. I think this is the first program in this learning process where I had to use a library.

```python
import re

email_pattern_reg = re.compile(r'[\w.-]+@[\w.-]+\.[\w]+')

def extract_emails(text):
    return email_pattern_reg.findall(text)

text = input("Enter the text you want to extract emails from")
print("Emails:", extract_emails(text))

```
In all these exercises, I got at least one error during the first run and those were all listed in the terminal with long descriptions. Those are unhandled exceptions. Now, how can we handle those exceptions? Below is the exercise I did for <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week2/exceptionHandling.py">exception handling</a>. Initially, I only handled one exception, ZeroDivisionError but what if the user gives a letter or string in place of a number? How can I handle that? I searched if there is a specific exception that I could use. I did not find any and I used a generic exception that would handle the rest of the exceptions and wrote the exception to the console.  

```python
def divideTwoNumbers(num1, num2):
    try:
        answer = num1 / num2
        return answer
    
    except ZeroDivisionError as e:
        return "Invalid. No number can be devided by zero"
    except Exception as e:
        return "An exception occured: " + str(e)


print(divideTwoNumbers(5, 2)) 
print(divideTwoNumbers(18, 0))
print(divideTwoNumbers(90, 'a')) 
print(divideTwoNumbers(40, 0.001)) 
```
The coming week, I plan to take some real time examples and explore all the challenges and would like to see to what extent I am able to handle those challenges without taking any online help. 



