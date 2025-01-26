#- - - Python Lists- - - - - - -
mylist = [1, 2, 3, 4, 5]
print(mylist)
print(len(mylist))

newList = list(("Hello", "World"))
print(newList)

#- - - Access List Items - - - -
print(newList[0],newList[-1])
print(mylist[1:3])
print(mylist[:-1])

if 1 not in mylist:
    print("there is no 1")
else:
    print("there is 1")

#- - - Change List Items - - - -
list1 = ["cherry", "strawberry", "blueberry", "melon"]
list1[-1] = "berry"
print(list1)

list1[1:3] = ["apple", "banana"]
print(list1)

list1.insert(1, "strawberry")
print(list1)

#- - - Add List Items- - - - -
list2 = ["apple", "banana", "cherry"]
list2.append("melon")
print(list2)

fruits = ["mango", "pineapple"]
list2.extend(fruits)
print(list2)


#- - - Remove List Items - - - -
list2.remove("apple")
list2.pop(0)
del list2[-1]
print(list2)

#- - - Loop Lists- - - - - - - -
nums = [1, 11, 2, 22, 3, 33]
for n in nums:
    print(n)

[print(x) for x in nums]

#- - - List Comprehension- - - -
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newFruits = []

for fruit in fruits:
    if "a" in fruit:
        newFruits.append(fruit)
print(newFruits)


newFruits1 = [fruit for fruit in fruits if "n" in fruit]
print(newFruits1)

newFruits1 = [x.upper() for x in newFruits1]
print(newFruits1)

#- - - Sort Lists- - - - - - - - -
nums.reverse()
print(nums)

nums.sort()
print(nums)

nums.sort(reverse = True)
print(nums)

#- - - Copy Lists - - - - - - - - -
thislist = ["apple", "banana", "cherry"]
MyList = thislist.copy()
print(MyList)

#- - - Join Lists - - - - - - - - -
l1 = [1, 2, 3, 4]
l2 = ["5", "6", "7", "8"]
for num in l1:
    l2.append(num)
print(l2)

#- - - List Methods - - - - - - - -
count = l1.count(1)
print(count)


