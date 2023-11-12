Number1 = int(input("Enter First Number: "))
Number2 = int(input("Enter Second Number: "))
Operator = input("Choose your operation: Addition(+), Subtraction(-), Multiplication(*), Division(/): ")

if Operator == "+":
    print(Number1 + Number2)
elif Operator == "-":
    print(Number1 - Number2)
elif Operator == "*":
    print(Number1 * Number2)
elif Operator == "/":
    print(Number1 / Number2)