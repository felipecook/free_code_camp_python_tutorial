# simple calculator app, takes in two inputted numbers and computes a desired operation

num1 = input("Please enter first number to be calculated: ")
num2 = input("Please enter the second number to be calculated: ")
operator = input("Please select the operator for these two numbers: ")

if operator == "*":
    print(float(num1) * float(num2))
elif operator == "/":
    print(float(num1) / float(num2))
elif operator == "+":
    print(float(num1) + float(num2))
elif operator == "-":
    print(float(num1) - float(num2))
else:
    print("operator is not recognized value of '+', '-', '/', or '*'.")




