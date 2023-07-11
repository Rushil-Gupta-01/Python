#Dictionaries is the storing of objects not in a ordered sequence
#They use curly braces {} and colons : to signify the keys and their associated value
    # {'key1':'value1','key2','value2'}
#Used when do not know the index position

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)

print(my_dict['key1'])

prices_lookup = {'apple':2.99,'orange':3.99,'mangoes':4.99}
print(prices_lookup['apple'])
print(prices_lookup['orange'])

dict = {'k1':123,'k2':[0,1,2,3,4],'k3':{'insidekey':200}}
print(dict['k3']['insidekey']) #Dictionaries are flexible in terms of what it can hold
print(dict['k2'])

print(dict['k2'][2]) 

d = {'key1':['a','b','c']}
mylist = d['key1']
print(mylist)

letter = mylist[2]
print(letter.upper())

print(d['key1'][2].upper()) #Easy method 
print(d['key1'][1].upper())

#Adding new keyword in a dictionary 
d = {'k1':100,'k2':200}
d['k3'] = 300

print(d)
d['k1'] = 50
print(d)

d = {'k1':100,'k2':200}
#To find all the keys:
print(d.keys())

#To find all the values:
print(d.values())

#To find the key and value in pair:
print(d.items())






