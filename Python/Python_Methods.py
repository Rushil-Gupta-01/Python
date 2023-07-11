lst = [1,2,3,4,5]

#Methods: append,count,extend,insert,pop,remove,reverse,sort

#append() allows us to add elements to the end of a list:
lst.append(6)
print(lst)

# The count() method will count the number of occurrences of an element in a list.
print(lst.count(2))
help(lst.count)

#Insert: This method is used to insert an element in a particular position of the exisiting list.
lst.insert(7,7)
print(lst)

#Extend: This method is used to append another list at the end of the list.

lst2 = [8,9,10]
lst.extend(lst2)
print(lst)

#Pop:
lst.pop()
print(lst)

#Reverse: This method is used to reverse the order of elemnts in the list.
lst.reverse()
print(lst)

#Remove: This method is used to remove first occurence of a given element from the existing list.
lst.remove(9)
print(lst)

#Sort: This method is used to sort the elements of the list into ascending order.
lst.sort()
print(lst)

