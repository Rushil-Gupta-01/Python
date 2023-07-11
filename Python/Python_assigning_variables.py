a = 5
#Now if I call a in my Python script,
#Python will treat it as the number 5.
print(a)

#What happens on reassignment? Will Python let us write it over?
#Reassignment:

a = 10
#checking
print(a)

#Re-defining a variable:
a = a + 5
print(a)


#The names you use when creating these labels need to follow a few rules:

    #1. Names can not start with a number.
    #2. There can be no spaces in the name, use _ instead.
    #3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
    #4. It's considered best practice (PEP8) that names are lowercase.
    #5. Avoid using the characters 'l' (lowercase letter el),'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
    #6. Avoid using words that have special meaning in Python like "list" and "str"

#Getting to know about the type of variable
print(type(a))