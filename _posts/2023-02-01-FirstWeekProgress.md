---
title: "First week's Progress"
date: 2023-02-01
---

In this week’s blog post, I will write about the progress I made last week in learning Python. Though I know a bit about Python, I wanted to learn from the basics, and now I realize that was a good decision. The reason for that is I have learned a lot of new things in the basics. However, it is interesting.

As of now, I have covered the basics like variables, data types, control structures, and functions. I started coding with a simple "Hello, World!" program. And I thought I will share how simple it is in Python when compared with C#.

In C# if I have to display “Hello, World!”. I have to write the code like this:

![image](https://user-images.githubusercontent.com/113061137/216233292-a5a149cf-799a-455b-a580-8ba37c725b06.png)

But to achieve the same thing in python the code looks as simple as plain English.

![image](https://user-images.githubusercontent.com/113061137/216228790-26207ffd-1517-4d53-889d-6954f95e2ced.png)

In addition to this, I have done the following tasks using python:

1.	Addition of two numbers
2.	Reverse an input string
3.	Concatenate two input strings
4.	Calculate the factorial of an input number
5.	Check if a given string is a palindrome


While doing the <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week1/AdditionOfTwoNumbers.py">addition of two numbers</a>, I was initially wrong as I added two inputs as strings instead of converting them to integers first. Later I found that I had to change them to integers and succeeded
```
a = input("number 1: ")
b = input("number 2: ")
print("sum is: " , int(a)+int(b))
```
For the second task, <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week1/ReverseString.py">string reversal</a>, I did not quite understand why we use [::-1] after the input string. Later, I searched the internet on how it works and got to know about slice notation. The concatenation task was again easy as there was nothing to typecast and just adding two inputs does the task. 
```
inputStr = input("Enter string: ")
reversedString = inputStr[::-1]
print("Reversed string is :  " , reversedString)
```

I did not quite want to jump into functions this week but the <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week1/factorialOfNumber.py">factorial</a> task was thrown at me and I had to use recursive functions directly. No regrets though, I understand what I wrote as I used functions in past. 

```
def calculateFactorial(num):
    if num == 1:
        return 1
    else:
        return num * calculateFactorial(num - 1)

input_number = int(input("Enter a number:"))

print("Factorial is  : ", calculateFactorial(input_number))
```

The <a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week1/palindrome.py">palindrome</a> task was easy again as I have already done the string reversal. Now, I just had to check whether the reversed string and the original string are the same or not.

```
inputString = input("Enter string: ")
reversedString = inputString[::-1]
if(inputString==reversedString):
    print("input is a palindrome")
else:
    print("input is not a palindrome")
 ```

After doing all these tasks, I definitely learned good basics in Python. One thing I am frustrated about in Python though is how everything changes with just one wrong indentation. 

In the next week, I plan to continue going deeper into Python and do some advanced tasks involving OOPS concepts.
