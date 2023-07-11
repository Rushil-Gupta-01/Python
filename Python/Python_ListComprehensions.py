mystring= 'hello'
mylist =[]
for letter in mystring:
    mylist.append(letter)
print(mylist)


myname = 'Rushil Gupta'
mylist = []
for letters in myname:
    mylist.append(letters)
print(mylist)


mylist = [letter for letter in mystring]
print(mylist)


mylist = [x for x in 'word']


mylist = [num for num in range(0,100)]
print(mylist)

mylist = [num**2 for num in range(0,5)]
print(mylist)


mylist = [x for x in range(0,10) if x%2==0]
print(mylist)

celcius = [0,10,20,34.5]
f = [((9/5)*temperatures + 32) for temperatures in celcius]
print(f)
#OR

fahrenheit = []
for temperatures in celcius:
    fahrenheit.append(((9/5)* temperatures + 32))

print(fahrenheit)

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)



mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(y-x)

    print(mylist)

mylist = [y-x for x in [2,4,6] for y in [100,200,300]]
print(mylist)

