a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if b == 0:
    raise ZeroDivisionError("hey divide by zero is not allowed")
else:
    print(f"the division is {a/b}")