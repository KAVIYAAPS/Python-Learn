a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=input("Enter operation (add, sub, mul, div): ")

if c == "add":
    result = a + b
elif c == "sub":
    result = a - b
elif c == "mul":
    result = a * b
elif c == "div":
    result = a / b
else:
    result = "Invalid input"

print(result)