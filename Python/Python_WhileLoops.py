#While Loops: Will continue to execute a block of code while some condition remains true.

#while some_boolean_condition:
    #Do something
#else:
    #do something different

x = 4
while x < 5:
    print(f'The current value of x is: {x}')
    x = x + 1

#break: break out of the current closest enclosing loop

mystring = 'Sammy'
for letter in mystring:
    if letter == 'm':
        break
    print(letter)

y = 0
while y < 10:
    if y == 2:
        break
    print(y)
    y += 1


#continue: goes to the top of the closest enclosing loop

mystring = 'Sammy'
for letter in mystring:
    if letter == 'm':
        continue
    print(letter)

#pass: does nothing at all

x = [1,2,3]
for item in x:
    #Comment
    pass 
print("End of my script")