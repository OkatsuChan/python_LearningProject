operator = input("Enter an operator (+,-,*,/): ")
num1 = float(input("Enter a number: "))
num2= float(input("Enter the second number: "))
compute = 0

if operator == "+":
    compute = num1 + num2
elif operator == "-":
    compute = num1 - num2
elif operator == "*":
    compute = num1 * num2
elif operator == "/":
    compute = num1 / num2
else:
    print(f"Invalid Operator you use {operator}")

print(f"Total computation for operator {operator} is {round(compute,3)}")