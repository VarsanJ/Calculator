import time
import math


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

x = 1
time.sleep(1)
print('Hello user! Welcome to the calculator!')
time.sleep(1)
print('This calculator currently supports addition, subtraction, multiplication, division, square roots and powers.')
time.sleep(1)

#loop
while x == 1:
    time.sleep(1)
    operation = input('''Please enter the operation that you would like to use. 
Enter help for more info and assistance. Enter exit to leave the system.''')

    if operation == 'addition' or operation == 'add' or operation == '+':
        print('Addition operation requested')
        an1 = input('Please enter number 1')
        an2 = input('Please enter number 2')
        try:
            an3 = float(an1)
            try:
                an4 = float(an2)
                sum = float(an1) + float(an2)
                print('The sum of {0} and {1} is {2}'.format(an3, an4, sum))
            except ValueError:
                print('The second number is not suitable.')
        except ValueError:
            print("The first number is not suitable")

    elif operation == 'subtraction' or operation == 'subtract' or operation == '-':
        print('Subtraction operation requested')
        an1 = input('Please enter number 1 ')
        an2 = input('Please enter number 2 ')
        try:
            an3 = float(an1)
            try:
                an4 = float(an2)
                sum = float(an1) - float(an2)
                print('The difference of {0} and {1} is {2}'.format(an3, an4, sum))
            except ValueError:
                print('The second number is not suitable.')
        except ValueError:
            print("The first number is not suitable")

    elif operation == 'multiplication' or operation == 'multiply' or operation == 'x' or operation == '*':
        print('Multiplication operation requested')
        an1 = input('Please enter number 1 ')
        an2 = input('Please enter number 2 ')
        try:
            an3 = float(an1)
            try:
                an4 = float(an2)
                sum = float(an1) * float(an2)
                print('The product of {0} and {1} is {2}'.format(an3, an4, sum))
            except ValueError:
                print('The second number is not suitable.')
        except ValueError:
            print("The first number is not suitable")

    elif operation == 'division' or operation == 'divide' or operation == '/':
        print('Division operation requested')
        an1 = input('Please enter number 1 ')
        an2 = input('Please enter number 2 ')
        try:
            an3 = float(an1)
            try:
                an4 = float(an2)
                if an4 == 0:
                    print('You can not divide by 0!')
                else:
                    sum = float(an1) / float(an2)
                    print('The quotient of {0} and {1} is {2}'.format(an3, an4, sum))
            except ValueError:
                print('The second number is not suitable.')
        except ValueError:
            print("The first number is not suitable")

    elif operation == 'exponent' or operation == 'power' or operation == '**':
        print('Exponential operation requested')
        an1 = input('Please enter number 1 (the base) ')
        an2 = input('Please enter number 2 (the exponent) ')
        try:
            an3 = float(an1)
            try:
                an4 = float(an2)
                sum = float(an1) ** float(an2)
                print('{0} to the power of {1} is {2}'.format(an3, an4, sum))
            except ValueError:
                print('The second number is not suitable.')
        except ValueError:
            print("The first number is not suitable")

    elif operation == 'square root' or operation == 'sqr' or operation == '//':
        print('Square root operation requested!')
        an1 = input('What number do you want the square root for? ')
        try:
            an2 = float(an1)
            an3 = math.sqrt(an2)
            print(f'The square root of {an2} is {an3}')
        except ValueError:
            print('0')

    elif operation == 'help':
        print(color.BOLD + color.UNDERLINE + 'Calculator Help' + color.UNDERLINE + color.END)
        print('''
This is a Calculator that would help you in your math questions.
The calculator currently supports addition, subtraction, multiplication, division and powers.

For addition, type addition, add or + when asked for input of operation
For subtraction, type subtraction, subtract and - when asked for input of operation
For multiplication, type multiplication, multiply, x or * when asked for input of operation
For division, type division, divide or / when asked for input of operation.
For powers, type exponent, power or ** when asked for input of operation.
For square root, type sqr, // or square root when asked for input of operation.

Entering invalid inputs for numbers in the equation may result in an error code and/or the system exiting.
When asked for the operation, you may also type exit for the system to shut down automatically.

Thank you for using the calculator!
            ''')
        time.sleep(2)

    elif operation == 'exit' or operation == 'leave':
        print('Exiting System')
        x = 2
        break

    else:
        print('Please enter a valid operation!')
        time.sleep(1)

print('The calculator is closing! Thank you for using the calculator!')
time.sleep(1)


# system closed