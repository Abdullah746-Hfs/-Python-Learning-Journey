num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operation = input("Enter the operation (+,-,*,/)")

if operation == "+":
    result = num1+num2
    print("Answer: ", result)
elif operation == "-":
    result = num1-num2
    print("Answer: ", result)
elif operation == "*":
    result = num1*num2
    print("Answer: ", result)
elif operation == "/":
    result = num1/num2
    print("Answer: ", result)
else:
    print>("Invalid operation. Please enter a valid operation (+, -, *, /).")
