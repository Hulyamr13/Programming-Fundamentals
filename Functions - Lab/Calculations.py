def calculation(operation, a, b):
    if operation == "multiply":
        return (a*b)
    elif operation == "divide":
        return int(a/b)
    elif operation == "add":
        return (a+b)
    elif operation == "subtract":
        return (a-b)

operator = input()
a = int(input())
b = int(input())

print(calculation(operator, a, b))