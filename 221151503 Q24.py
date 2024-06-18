def simple_calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operator (+, -, *, /): ")

result = simple_calculator(number1, number2, operation)
print(f"The result is: {result}")
