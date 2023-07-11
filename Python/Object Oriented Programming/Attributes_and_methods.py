class Dog(): #Capital Casing

    #CLASS OBJECT ATTRIBUTE
    # Same for any instance

    species = 'mammal'

    
    def __init__(self,mybreed,name):
        #Attributes
        #We take in the arguments
        #Assign it using self.attribute_name
        self.mybreed = mybreed #String
        self.name = name #String
       
    
    #Operations/Actions ----> Methods:
    def bark(self):
        print("Woof! My name is {} and my breed is {}".format(self.name, self.mybreed))
        

my_dog= Dog(mybreed = "Lab", name = "Aayush")
print(type(my_dog))

print(my_dog.mybreed)
print(my_dog.name)

print(my_dog.species)

#Methods
my_dog.bark()


class Circle():
    #Class object attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius *self.pi #Or use Circle.pi

    #Method:
    def get_circumference(self):
        return self.radius * self.pi * 2

    
my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)

print(my_circle.get_circumference())