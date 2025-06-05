name = input("Hello, Enter your name please?\n")
print('Welcome to the calculator, '+ name + '!')

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def modulus(a,b):
    return a % b

try:
    a = int(input('Enter first value: '))
    b = int(input('Enter second value: '))
    op = input('operator: ')

    if op == '+':
        print(add(a,b))
    elif op == '*':
        print(multiply(a,b))
    elif op == '-':
        print(subtract(a,b))
    elif op == '/':
        print(divide(a,b))
    elif op == '%':
        print(modulus(a,b))
    else:
        print('Invalid operator entered.')
except Exception:
    print("Invalid coordinates entered.")




