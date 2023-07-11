
class Dog(): #Capital Casing
    
    def __init__(self,mybreed,name,spots):
        #Attributes
        #We take in the arguments
        #Assign it using self.attribute_name
        self.mybreed = mybreed #String
        self.name = name #String
        #Expect boolean True/Flase
        self.spots = spots #Boolean

my_dog = Dog(mybreed = "Lab")
print(type(my_dog))

print(my_dog.mybreed)


my_dog= Dog(breed = "Lab", name = "Aayush", spots = True)
print(type(my_dog))

print(my_dog.mybreed)
print(my_dog.name)
print(my_dog.spots)









