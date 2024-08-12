def add (x, y):
    return x + y

def subtract (x, y):
    return x - y
def Mutiply (x, y):
    return x * y

def divide (x, y):
    return x / y

print("Select the operation.")
print("1.add")
print("2.Subtract")
print("3.Mutiply")
print("4.Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))

        if choice == '1':
            print(num1, "+", num2, "+", num3, "=", add(num1, num2,))

        elif choice == '2':
            print(num1, "-", num2, "-", num3, "=", subtract(num1, num2,))

        elif choice == '3':
            print(num1, "*", num2, "*", num3, "=", Mutiply(num1, num2,))

        elif choice == '4':
            print(num1, "/", num2, "/", num3, "=", divide(num1, num2,))

        next_calculation = input("'let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

        else:
            print("Invalid input")