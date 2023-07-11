#LEGB RULE:
#L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

#E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

#G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

#B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...

from re import X


x = 25
def printer():
    x = 50
    return x 

print(x)
print(printer())

lambda num: num **2 #LOCAl


name = "This is a global string" #Global 
def greet():
    name = 'Sammy' #Enclosing
    def hello():
        print('Hello ' + name)
    
    hello()
greet()

def greet():
    def hello():
        name = 'I am local' #Local
        print("Hello "+ name)
    hello()

greet()



x = 50
def func(x):
    print(f"X is {x}")

func(x)


x = 50
def func(x):
    print(f"X is {x}")
    x = 200
    print(f"I just locally chnaged X to {x}")

func(x)

print(x)


y = 100
def func():
    global y #Will effect the golbal variable
    print(f'Y ix {y}')

    #Local Reassignment on a global variable!
    y = 'New Value'
    print(f"I just locally chnaged Global Y to {y}")


print(y)
func()

print(y)

z = 200
def func(z):
    print(f"Z is {z}")

    z = 'New Value'
    print(f"I just changed Z to {z}")
    return z

func(z)
z = func(z)
print(z)