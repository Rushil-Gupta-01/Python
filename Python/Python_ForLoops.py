my_iterable = [1,2,3,4,5]
for item_name in my_iterable:
    print(item_name)

my_family = ['Rushil','Aayush','Vikas','Vandana']
for family_memebers in my_family:
    print(family_memebers)

mylist = [1,2,3,4,5,6,7,8,9,10]
for numbers in mylist: 
    print(numbers)

for num in mylist:
    #Check for even
    if num % 2 == 0:
        print(f'Even Number: {num}')
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num 

    print(list_sum)

print(list_sum)

mystring = 'Hello World'
for letter in mystring:
    print(letter)

    #Or
for letter in 'Hello World':
    print(letter )

tup = (1,2,3)
for num in tup:
    print(num)

mylist = [(1,2),(3,4),(5,6),(7,8)]
for tuples in mylist:
    print(tuples)

    #OR

for (a,b) in mylist: #tuple unpacking
    print(a)
    print(b)

mylist = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in mylist:
    print(a,b,c)

d = {'k1':1,'k2':2,'k3':3}
for items in d.items():
    print(items)
for key,value in d.items():
    print(key,value)

