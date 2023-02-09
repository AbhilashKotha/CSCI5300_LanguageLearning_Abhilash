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