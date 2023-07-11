from math import sqrt

user_name = str(input('What is your name? '))

while True:
    print('\nHi {0}! What do you want to do?'.format(user_name))
    print("1 => Addition")
    print("2 => Subtraction")
    print("3 => Division")
    print("4 => Multiplication")
    print("5 => Square Root")
    print("6 => Square")
    print("7 => Find the power to a number")
    print("8 => Random Number")
    print("Enter Q or q to Exit!")

    operation = input('Enter you choice: ')
    if operation == 'q' or operation == 'Q':
        print("\n=> Thank You!")
        break
        

#Addition
    if operation == '1':
        number1 = float(input('Enter your first number: '))
        number2 = float(input('Enter your second number: '))
        sum = number1 + number2
        print('\n=>The sum of {0} and {1} is: {2}'.format(number1,number2,sum))

#Subtraction
    elif operation == '2':
        number1 = float(input('Enter your first number: '))
        number2 = float(input('Enter your second number: '))
        difference = number1 - number2
        print('\n=>The difference between {0} and {1} is: {2}'.format(number1,number2,difference))

#Division
    elif operation == '3':
        number1 = float(input('Enter your first number: '))
        number2 = float(input('Enter your second number: '))
        quotient = number1 / number2
        print('\n=>The quotient when {0} is divided by {1} is: {2}'.format(number1,number2,quotient))

#Multiplication
    elif operation == '4':
        number1 = float(input('Enter your first number: '))
        number2 = float(input('Enter your second number: '))
        product = number1 * number2
        print('\n=>The product of {0} and {1} is: {2}'.format(number1,number2,product))

#Square Root
    elif operation == '5':
        number1 = float(input('Enter your number: '))
        squareRoot = sqrt(number1)
        print('\n=>The square root of {0} is: {1}'.format(number1,squareRoot))

#Square
    elif operation == '6':
        number1 = float(input('Enter your number: '))
        square = number1**2
        print('\n=>The square of {0} is: {1}'.format(number1,square))

#Finding the power to a number
    elif operation == '7':
        number1 = float(input('Enter your first number: '))
        number2 = float(input('Enter your second number (power): '))
        power = number1**number2
        print('\n=>{0} raised to the power {1} is: {2}'.format(number1,number2,power))

        
#Random Number
    elif operation == '8':
        number1 = float(input('Minimum (Range):  '))
        number2 = float(input('Maximum (Range):  '))
        from random import randint
        randomno= randint(number1,number2)
        print('\n=>The Random number generated is: {0}'.format(randomno))




    else:
        print('\n=>Invalid Choice')





    





