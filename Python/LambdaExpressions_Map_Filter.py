def square(num):
    return num ** 2

my_num = [1,2,3,4,5]

map(square,my_num)
for item in map(square, my_num):
    print(item)

print(list(map(square,my_num)))

def splicer(mystring):
    if len(mystring)%2 ==0:
        return 'EVEN'
    else:
        return mystring[0]

name = ['Andy','Eve','Sally']

print(list(map(splicer,name)))


def check_even(num):
    return num%2==0

mynum = [1,2,3,4,5,6,7,8,9]
print(list(filter(check_even,mynum)))

for n in filter(check_even,mynum):
    print(n)


#Original 
def sqaure(num):
    result = num**2
    return result

print(square(3))

#LambdaExpression
sq = lambda num : num**2
print(sq(5))



#Line 1 to Lambda Expression

map(lambda num : num**2, my_num)
for n in map(lambda num : num**2, my_num):
    print(n)

#Line 23 to Lambda Expression:

filter(lambda num: num%2==0,mynum)
for n in filter(lambda num: num%2==0,mynum):
    print(n)



map(lambda name: name[0],name)
for n in map(lambda name: name[0],name):
    print(n)

map(lambda name:name[::-1],name)
for n in map(lambda name:name[::-1],name):
    print(n)



