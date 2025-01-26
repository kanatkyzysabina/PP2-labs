#- - - Python Sets- - - - - - - -
s1 = {"apple", "banana", "cherry", "apple"}
print(s1)

s2 = {"apple", 1, True, 0, "56"}
print(s2)

s1 = set(("apple", "banana", "cherry"))
print(s1)

#- - - Access Set Items - - - - -
for s in s1:
    print(s)

#- - - Add set items- - - - - - -
thisSet = {"apple", "banana", "cherry"}
thisSet.add("orange")
print(thisSet)

tropical = {"pineapple", "mango", "papaya"}
thisSet.update(tropical)
print(thisSet)

thisList = ["cherry", "blueberry"]
thisSet.update(thisList)
print(thisSet)

#- - - Remove Set Items- - - - - -
thisSet.remove("banana")

thisSet.discard("apple")
print(thisSet)

#- - - Loop Sets - - - - - - - - -

for x in thisSet:
    if "a" in x:
        print(x)

#- - - Join Sets- - - - - - - - - -
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set3 = set1 | set2
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2  #difference()
print(set3)

