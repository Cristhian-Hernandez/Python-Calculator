# My simple Python Calculator

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

working = 0
choosing = 0
choices = ["add", "sub", "mult", "div"]

print("Hello! I am calculatron3000, your favourite calculator.\n")

while working == 0:
    print("I can help you with Addition, Substraction, Multiplication and Division\n")

    choice = str(input("So which are you going to choose today?\n(Type add, sub, mult or div)\n --> "))

    if choice in choices:
        print("Wonderful!")
        print("Now we need two numbers for the operation.\n")
    else:
        choosing += 1
        while choosing == 1:
            print("Invalid input, check your spelling and try again.\n")
            choice = str(input("So which are you going to choose today?\n(Type add, sub, mult or div)\n --> "))
            if choice in choices:
                choosing -= 1
                print("Wonderful!")
                print("Now we need two numbers for the operation.\n")
    
    num1 = int(input("Type in the first number:\n -->"))
    num2 = int(input("Type in the second number:\n -->"))
    
    if choice == 'add':
        print(num1,"+",num2,"=", add(num1, num2)) 
    elif choice == 'sub':
        print(num1,"-",num2,"=", substract(num1, num2))
    elif choice == 'mult':
        print(num1,"*",num2,"=", multiply(num1, num2))
    elif choice == 'div':
        print(num1,"/",num2,"=", divide(num1, num2))

    print("That was easy!")
    help = str(input("Do you need help with anything else? (Use yes or no)\n --> "))
    
    if help != 'yes':
        print("\nOh :(\nSee you later my friend!")
        working += 1
    else:
        continue
