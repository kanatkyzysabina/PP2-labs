#- - - Python Data Types- - - - - -
x = True #setting the data type
y = "String"
z = 3.5

x = bool(False) #specifying data type
y = str("String")
z = float(3.5)
print(type(x))
print(type(y))
print(type(z))


#- - - Python Numbers- - - - - - - 

x = 11  #int
y = 2.2 #float
z = 33j  #complex

#conversion to another numeric data type
a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

#random number

import random
print(random.randrange(1, 5))


#- - - Python Casting- - - - - - -

x = int(11)   # x will be 11
y = int(22.2) # y will be 22
z = int("33") # z will be 33
print(x)
print(y)
print(z)