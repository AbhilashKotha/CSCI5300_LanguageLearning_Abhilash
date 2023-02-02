def calculateFactorial(num):
    if num == 1:
        return 1
    else:
        return num * calculateFactorial(num - 1)

input_number = int(input("Enter a number:"))

print("Factorial is  : ", calculateFactorial(input_number))
