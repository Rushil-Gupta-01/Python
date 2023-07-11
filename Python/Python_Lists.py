# Lists use [] square brackets

from hashlib import new


my_list = [1,2,3]
my_list = ['String',100,10.2]

print(len(my_list))

mylist = ['one', 'two', 'three']
print(mylist[1])

another_list = ['four', 'five', 'six']

new_list = mylist + another_list
print(new_list)

print(new_list[5])
print(new_list[1:3])

new_list[0] = 'ONE'  #List are mutable
print(new_list)

list = [1,2,3,4,5,6]
second_list = [7,8,9]

newlist = list + second_list
print(newlist)

newlist.append(0) #Adding onto the list 
print(newlist)

newlist.pop() #Removing from the list
print(newlist)

popped_item = newlist.pop()
print(popped_item)

newlist.pop(1)
print(newlist)

newlist.pop(-1)
print(newlist)

new_list = ['a','e','x','b','c']
num_list = [4,1,8,3,2,9]

new_list.sort()
print(new_list)
#Sorting
num_list.sort()
print(num_list)

new_list.reverse()
print(new_list)
#Reversing 
num_list.reverse()
print(num_list)


