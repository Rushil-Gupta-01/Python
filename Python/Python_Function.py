#//def keywords:
   #=> def name_of_function():

from tabnanny import check


def greet(first_name,last_name):
    print(f'Hi {first_name} {last_name}')
    print("Welcome abord")
greet('Rushil','Gupta')


def say_hello():
    print("Hello")

say_hello() #Calling out a function

def say_hello(name= 'None'):
    print(f'Hello {name}')

say_hello('Rushil')
say_hello()

#Print
def print_result(a,b):
    print(a+b)
print_result(10,10)
result = print_result(10,10) #Now when we call out result we would not get an output as print syntax can't save the result

#Return
def return_result(a,b):
    return a+b
print(return_result(10,20))
result = return_result(10,20) #Result syntax saves the result so now it can be provided a variable and be called later in the programme with that variable
print(result)

#Print+Return  => Rare 
def myfunc(a,b):
    print(a+b)
    return(a+b)
result = myfunc(10,50)
myfunc(10,50)
print(result)

#Possible Bugs:
def sum_numbers(num1,num2):
    return num1+num2

print(sum_numbers(10,90))
print(sum_numbers('10','90'))



#//Logic With Functions:
print(2%2)
print(20 % 2 ==0)

def even_check(num):
   return num%2==0
print(even_check(70))

#Return true if any number is even inside a list
def check_even_list(num_list):
    for number in num_list:
        if number %2 ==0:
            return True
        else:
            pass

print(check_even_list([1,2,3,4,5]))
print(check_even_list([1,3,5]))


def check_odd_list(num_list):
    for numbers in num_list:
        if numbers %2 != 0:
            return True
        else:
            pass
           # return false  => Wrong!!
    return False #This is because the return statement breaks the code and if we put the syntax "return False" there it will not check the whole code rather would check only the first digit


print(check_odd_list([1,3,5,7,9]))
print(check_odd_list([2,4,6,8]))



def check_user_evenlist(num_list):
    #Return all the even numbers in a list
    even_numbers = []
    
    for numbers in num_list:
        if numbers%2==0:
            even_numbers.append(numbers)
        
        else:
            pass
    return even_numbers

print(check_user_evenlist([1,2,3,4,5,6]))
print(check_user_evenlist([1,3,5]))


#//Tuple Unpacking With Python Functions
stock_prices = [('AAPPLE',200),("GOOGLE",300),("MICROSOFT",500)]

for items in stock_prices:
    print(items)

for company,price in stock_prices: #Tuple unpacking
    print(company)
    print(price)


work_hours = [("Rushil",100),("Billy",200),("Cassie",350)]
def employee_check(work_hours):
    current_max = 0
    employee_of_the_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass

    return(employee_of_the_month,current_max)
result = employee_check(work_hours)
print(result)

name,hours = employee_check(work_hours)
print(result)
print(name)
print(hours)



#//Interaction b/w Functions;
#Check FindTheBall_game.py


#//*args and **kwargs in python
def myfunc(a,b):
    #Retuns 5% of the sum of an and b
    return sum((a,b))*0.05
print(myfunc(40,60))


def myfunc(a,b,c=0,d=0,e=0):
    #Retuns 5% of the sum of an and b
    return sum((a,b,c,d,e))*0.05
print(myfunc(40,60,100))


def myfunc(*args):
    return sum (args)*0.05 #To add infinite arguments in the tuple to follow the parameters in that function
print(myfunc(40,5,505,50,5,59,59,99,1000))


def myfunc(**kwargs):
    if 'fruits' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruits']))
    else:
         print("I did not find any fruits here")

print(myfunc(fruits = 'apple',veggie = 'lettuce'))


def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0],kwargs['food']))
print(myfunc(10,20,30,fruits = 'roange',food = 'waffles'))



