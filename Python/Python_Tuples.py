#Tuples are very similar to list but are immutable meaning they can't be edited

#Tuples
t = (1,2,3)
print(type(t))
print(len(t))
print(t[1])

#Lists
l =  [1,2,3]
print(type(l))
print(len(l))
print(l[1])


t = ('a','a','a','b')
print(t.count('a'))
print(t.index('b'))

print(t)
print(l)

l[0] = 0 #lists are muatble
print(l)

t[0] = 0
print(t) #Will give us an error as strings are immutable
