#Strings
#Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).

#This idea of a sequence is an important one in Python and we will touch upon it later on in the future.

#In this lecture we'll learn about the following:

#1.) Creating Strings #2.) Printing Strings
#from re import L
#from tkinter import N


from email.errors import InvalidBase64CharactersDefect


print('Using Single quotes')
print("Using double quote")
#print(' I'm using single quotes, but this will create an error') Will give an error
print(" I'm using single quotes, but this will create an error")

    #Adding next line
print("Rushil \n Gupta")
print("Rushil \nGupta")

    #Finding the number of characters
print(len("Rushil"))

#3.) String Indexing and Slicing
    #Indexing
mystring = "Hello World"
print(mystring)

print(mystring[7]) #Postive indexing
print(mystring[-2]) #Negative indexing 

    #Slicing
mystring = "abcdefghijklmno"
print(mystring[2:])#Starting index

print(mystring[:3]) #Go upto but do not include, here 3(here d)

print(mystring[3:6])
print(mystring[1:3])
print(mystring[3:9])

print(mystring[::]) #Start to end 
    #Adding steps:
print(mystring[::3])

    #Eg. 
print(mystring[1:7:2]) #Start:Stop:End

#Reversing the string:
print(mystring[::-1])


#Concatenate String:
name = "Pam"
#print(name[0] = "S")

    #Error

print(name[1:])
print('S' + name[1:])

x = 'Hello World '
print(x + 'it is beautiful outside')

x = x + 'it is beautiful outside'
print(x)

name = "Sushil"
last_letter =name[1:]
print("R"+ last_letter)








letter = "/"
print(letter*10)


#Uppercase

x = "Rushil Gupta"
print(x.upper()) #Need to add open and end paranthesis #Here x is a variable

#Lowercase

x = "Rushil Gupta"
print(x.lower()) #Need to add open and end paranthesis 

y = "rushil gupta"
print(y.upper())
print(y.lower())


#Split - Creating and instant list
print(y.split()) 

print(y.split("l")) #When need to split at particular letter

#String Formatting
#Formatting with {}'.format() method:

print("This is a string {}".format('Inserted.'))
print('The {} {} {} '.format('fox', 'brown', 'quick'))
print('The {2} {1} {0} '.format('fox', 'brown', 'quick')) #With index positions
print('The {q} {b} {f} '.format(f='fox', b='brown', q='quick')) #More preferable.

print("My name is {f} {l}".format(f='Rushil', l ='Gupta.'))

result = 100/888
print(result)

print('The result was {}'.format(result))
print('The result was {r:1.5f}'.format(r=result))

#f strings method

name = 'Rushil'
print(f'Hello, his name is {name}')
age = 14

print(f'{name} is {age} years old')

name = 'Rushil Gupta'
age = 15
school = 'Salwan Public School'

print(f'{name} of {age} years studies in {school}.')

