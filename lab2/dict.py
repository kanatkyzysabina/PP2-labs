#- - -Python Dictionaries- - - - - - -
thisdict = {"brand":"Ford", "model":"Mustang","year":1964}
print(thisdict)
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict["colors"][0])

#- - - Access Items- - - - - - - - -
x = thisdict.get("year")
print(x)

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)

#- - - Change Items- - - - - - - - 
thisdict["year"] = 2018
print(thisdict["year"])

thisdict.update({"year": 2020})
print(thisdict["year"])

#- - -Add Items- - - - - - - - - -
thisdict.update({"color": "red"})

thisdict["color"] = "red"

print(thisdict)

#- - - Remove Items- - - - - - - -
thisdict.pop("color")
print(thisdict)

del thisdict["brand"]
print(thisdict)


#- - - Loop Dictionaries- - - - - 
for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x, y in thisdict.items():
  print(x, y)

#- - - Copy Dictionaries- - - - -
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

#- - - Nested Dictionaries- - - -
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
print(myfamily["child1"]["name"])





