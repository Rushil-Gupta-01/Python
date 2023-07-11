#Sets are unordered collections of unique elements. Meaning that there can be only be one rep. of the same obj
myset = set()
myset.add(1)
print(myset)

myset.add(2)
print(myset)

myset.add(2)
print(myset)#Will not add another 2

my_list = [1,1,1,1,2,2,3,3,3,4,4,4,5,5,6,6,6,7,7,7,8,8,8,9,0,0,0,0]
print(set(my_list)) #Don't have a particular order

