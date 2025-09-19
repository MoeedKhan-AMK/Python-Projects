'''🔹 2. Simple Calculator

-Build a calculator that performs:
-Addition, subtraction, multiplication, division.
-Maybe extend it to handle power (^) and square root.
-Use functions for cleaner code.
'''

import math


#Defining Calculate Function rules:

def calculate(n1,n2,operator):
    if operator == "+":
        return  n1 + n2
    elif operator == "-":
        return  n1 - n2
    elif operator == "*":
        return  n1 * n2
    elif operator == "/":
        if n2 ==0:
            return "Error! Division by zero."
        return  n1 / n2
    elif operator == "^":
        return  n1 ** n2
    elif operator == "root":
        return math.sqrt(n1)
    else:
        return "Invalid Operator"
    
    # return result
#User Input

num1 = float(input("Enter Number:"))
operator = input("Choose Operation (+, -, *, /, ^, root): ").lower()

#ask for second number if operator is not root
if operator != "root":
    num2 = float(input("Enter Number:"))
else:
    num2 = None


#Calculating Result
result = calculate(num1, num2, operator)
print('Result =',result)

