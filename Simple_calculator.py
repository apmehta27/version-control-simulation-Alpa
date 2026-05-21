print("Part 2")

input_number_1 = input("Enter the first number: ")
input_number_2 = input("Enter the second number: ")
operation = input("choose an operation (+, -, *, /): ")
# Check if inputs are numeric
if not input_number_1.replace('.', '', 1).isdigit() or not input_number_2.replace('.', '', 1).isdigit():
    print("Error: Please enter valid numeric values.")
else:
    # Convert inputs to numbers
    num1 = float(input_number_1)
    num2 = float(input_number_2)

if operation == "+":
    result = num1 + num2
    print("The sum of the two numbers is " + str(result) + ".")
elif operation == "-":
    result = num1 - num2
    print("The difference of the two numbers is " + str(result) + ".")
elif operation == "*":
    result = num1 * num2
    print("The product of the two numbers is " + str(result) + ".")
elif operation == "/":
    result = num1 / num2
    print("The quotient of the two numbers is " + str(result) + ".")
elif operation != "+" and operation != "-" and operation != "*" and operation != "/":
    print("Invalid operation. Please choose one of the following: +, -, *, /.")