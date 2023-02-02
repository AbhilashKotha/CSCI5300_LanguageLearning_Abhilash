inputString = input("Enter string: ")
reversedString = inputString[::-1]
if(inputString==reversedString):
    print("input is a palindrome")
else:
    print("input is not a palindrome")