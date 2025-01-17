#- - - Python Variables - - - - - - - - - -
x = 2
y = "string"
print(x)
print(y)

#casting
z = str(3)
z1 = int(4)
print(type(z)) #function to get data type of a variable



#- - - Variable Names - - - - - - - - - - -
#legal names:
my_var = "variable"
myvar = "variable"
MyVar = "variable"
MYVAR = "variable"
my_var_1 = "variable"



#- - - Assign Multiple Values - - - - - - -
x, y, z = "Apple", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits #unpacking
print(x)
print(y)
print(z)



#- - - Output Variables - - - - - - - - - -
x = "i "
y = "love "
z = "cats "
print(x, y, z)
print(x + y + z)



#- - - Global Variables - - - - - - - - - -

x = "cats " #global
def stateFact():
    x = "dogs " #local
    print(x + "are " + "super " + "cute!")

stateFact()
print(x + "are " + "super " + "cute!")

def myFunc():
    global x #now x belongs to global scope
    x = "cats "
    print(x + "are " + "cute!")

myFunc()
print(x + "are " + "cute!")


