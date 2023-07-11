mylist = [1,2,3,4]

for num in range(5,10,2): #(Start from , And not include, Step size)
    print(num)


print(list(range(0,11,2)))

index_count = 0
for letter in 'abcdefghijkl':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

index = 0 
for letter in 'Rushil':
    print(f'At index {index} the letter is {letter} ')
    index += 1

word = 'Rushil'
for index,item in enumerate(word):
    print(index,item)


mylist = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
mylist3 = [100,200,300,400,500]

for items in zip(mylist,mylist2,mylist3):
    print(items)

list(zip(mylist,mylist2,mylist3))

print('x' in [1,2,3])
print(2 in [1,2,3])

print('a' in 'a world')
print('mykey' in {'mykey':123})
d = {'mykey':345}
345 in d.items()

mylist = [1,2,3,4,5,6]
print(min(mylist))
print(max(mylist))

#Random Liberary:
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))


#Accepting user input
import math 
num_1= int(input('Enter your first number here: '))
num_2= int(input('Enter your second number here: ')) #Answer is in string form
operation = input('Choose your operation (+,-,/,*,sqrt,sq): ')

if operation == '+':
    print(num_1 + num_2)

if operation == '-':
    print(num_1 - num_2)

if operation == '/':
    print(num_1 / num_2)

if operation == '*':
    print(num_1 * num_2)

if operation ==  'sqrt':
    square = math.pow(num_1,0.5)
    print('The square root of the given number {0} = {1}'.format(num_1,square))

if operation == 'sq':
    sq = num_1 **2
    print("The square of the given number {0} is: {1}".format(num_1,sq))