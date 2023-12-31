# this program is a basic calculator
# define the functions: add, sub, mul, div
# shows the options available to the user
# ask for values
# call the functions

def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) +"\n")

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) +"\n")

def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer) +"\n")

def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer) +"\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Enter your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a,b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Program Ended!")
        quit()







