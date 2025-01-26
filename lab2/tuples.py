#- - - Python Tuples- - - - - - - - 

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#- - - Access Tuples- - - - - - - -
thistuple = ("apple", "banana", "cherry")
print(thistuple[:-1])

#- - - Update Tuples - - - - - - - -
mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
mylist[1] = "kiwi"
mytuple = tuple(mylist)

print(mytuple)

#- - - Unpack Tuples- - - - - - - - -
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#- - - Loop Tuples- - - - - - - - - -
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i += 1

#- - - Join Tuples- - - - - - - - - -
fruits1 = ("apple", "banana", "cherry")
mytuple = fruits1 * 2

print(mytuple)