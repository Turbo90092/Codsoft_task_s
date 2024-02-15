
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a // b

print(''' select opration:"
          1 .Add
          2. Subtract
          3. Multiply
          4. Divide
          5. exit
''')

while True:

    selection = input('> ')

    if selection == '5':
        exit()

    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    if selection == '1':
        print(f" = {add(num1,num2)}")
    elif selection == '2':
        print(f" = {subtract(num1,num2)}")
    elif selection == '3':
        print(f" = {multiply(num1,num2)}")
    elif selection == '4':
        if num2 == 0:
            print('error: can not divide by zero')
        else:
            print(f" = {divide(num1,num2)}")
    else:
        print('invalid input')






