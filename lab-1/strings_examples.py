#- - - Python Strings- - - - - - - - -

a = "Hello"
a = "It's nice" #quotes inside quotes
print(a)

a = """This is
Multiline string!""" #multiline string
print(a)

a = "Hello"
print(a[0])

for x in "word": #looping through string
    print(x)

print(len(a)) #length of a string

#Check String
print("H" in a)
print("H" not in a)



#- - - Slicing Strings- - - - - - - -

b = "i love cats"
print(b[2:6])
print(b[:6])
print(b[0:])
print(b[-1]) #outputs last letter



#- - - Modify Strings- - - - - - - -
a = "hello"
b = "HELLO"
print(a.upper())
print(b.lower())
print(a.replace("h", "y"))

a = "Hello, world"
print(a.split(","))


#- - - Concatenate Strings- - - - - -
a = "hello"
b = "world"
c = a + " " + b
print(c)

#- - - Format Strings - - - - - - - -

age = 18
print(f"Im {age} years old")
print(f"im {9*2} years old")

print(f"the price is {age:.2f}$")


#- - - Escape Characters- - - - - - -

s = "name of the movie is \"Maze Runner\"."
print(s)


#- - - String Methods- - - - - - - - -
txt = "hello, world"
print(txt.capitalize())
print(txt.count("l"))
print(txt.find("h"))
