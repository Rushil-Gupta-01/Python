my_file = open('test.txt', 'w+')
my_file.write('Python is an object oriented programming language.')

my_file.seek(0)
print(my_file.read()) #Read a txt file in python

my_file.close() #always do this when you're done with a file


#Appending to a File
my_file = open('test.txt','a+')
my_file.write("\n This is text being appended to test.text")
my_file.writelines("\n And another line here. \n We can add multiple line through the .writlines syntax.")

my_file.seek(0)
print(my_file.read())
my_file.close()



mode = 'r' #Is read only
mode = 'w' #is write ony (will overwrite files or crate new)
mode = 'a' #IS append only (will add on to files)
mode = 'r+' #Is reading n writing
mode = 'w+' #is writing n reading (Overwriting existing files or creates a new file.)

file = open('testrun.txt', 'w+')
file.write('This is the first string.\n This is the second string.')

file.seek(0)
print(file.read())
file.close()