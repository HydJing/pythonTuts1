num1 = float(input("enter first number"))
op = input("operator")
num2 = float(input("enter second number"))

result = 0
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2
else:
    result = "invalid operator"

print(result)