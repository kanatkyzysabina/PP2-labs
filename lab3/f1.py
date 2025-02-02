#1- - - - - - -
def converter(ounces):
    grams = ounces/28.3495231
    print(grams, "ounces")

ounces = int(input("Print number in grams: "))
converter(ounces)


#2- - - - - - -
def tempConverter(F):
    C = (5/9)*(F-32)
    print(f"Temperature in Celcius is: {C}")

F = float(input("Print number in Farenheits: "))
tempConverter(F)


#3- - - - - - -
def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbits = numheads - chickens
        if 2*chickens + 4*rabbits == numlegs:
            print(f"There is {chickens} chickens and {rabbits} rabbits in a farm")
            break
numheads = 35
numlegs = 94
solve(numheads, numlegs)


#4- - - - - - - 
def isPrime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def FilterList(inputlist):
    res = []
    for x in inputlist:
        if isPrime(int(x)):
            res.append(x)
    return res

inputlist = list(input("Please enter numbers for your list: ").split())
print("Prime numbers from a list: ")
for i in FilterList(inputlist):
    print(i)


#5- - - - - - - 


def permute(inputs):
    if len(inputs) == 1:
        return inputs
    
    result = []

    for i in range(len(inputs)):
        letter = inputs[i]
        x = inputs[:i] + inputs[i+1:]
        for p in permute(x):
            result.append(letter + p)
    return result

inputStr = str(input("Enter any word: "))

finalList = permute(inputStr)

for f in finalList:
    print(f)


#6- - - - - - - 

def StringReverser(words):
    reversedW = words[::-1]
    print("Reversed List: ", reversedW)


words = input("Enter words: ").split()
StringReverser(words)



#7- - - - - - -


def has_33(inputList):
    x = False
    for i in range(len(inputList)):
        if int(inputList[i]) == 3:
            if int(inputList[i+1]) == 3:
                x = True
                break
    return x

IntsList = list(input("Print any numbers for a list: ").split())

if has_33(IntsList):
    print("The list contains consecutive 3s!")
else:
    print("The list does not contain consecutive 3s((")



#8- - - - - - -


def spy_game(nums):
    secret_code = [0, 0, 7]
    i = 0
    for n in nums:
        if i < len(secret_code) and n == secret_code[i]:
            i += 1
    return i == len(secret_code)


integers = input("Print your list for a spy game: ")
nums = list(map(int, integers.split()))
if spy_game(nums):
    print("The capture of the spy was successful!!")
else:
    print("The capture of the spy was unsuccessful((")



#9 - - - - - -

def Calculate_Volume(radius):
    volume = (4/3) * (radius**3)
    print(f"{volume}π cm^3")

r = float(input("Enter radius of a sphere: "))
print("Volume of a sphere(without approximated pi): ")
Calculate_Volume(r)

#if π ≈ 3.14:

def Calculate_Volume(radius):
    volume = (4/3) * (radius**3) * 3.14
    print(f"{volume} cm^3")

r = float(input("Enter radius of a sphere: "))
print("Volume of a sphere: ")
Calculate_Volume(r)


#10 - - - - - -

def make_unique(thisList):
    result = []
    for n in thisList:
        n = int(n)
        if n not in result:
            result.append(n)
    print(result)

thisList = input("Enter numbers for a list: ").split()
make_unique(thisList)


#11 - - - - - - 

def Check_Palindrome(input_string):
    is_p = True
    for i in range(len(input_string)//2):
        if input_string[i] != input_string[len(input_string)-i-1]:
            is_p = False
            break
    return is_p

word = input("Enter any word: ")
if(Check_Palindrome(word)):
    print("Your word is a palindrome!")
else:
    print("Your word is not a palindrome(((")


#12- - - - - - -

def histogram(nums):
    for n in nums:
        print("*" * n)


nums = input("Enter numbers for a list: ")
nums_list = list(map(int, nums.split()))
histogram(nums_list)



#13- - - - - - -
import random


def GuessNum_Game():
    print("Hello! What is your name?")
    name = input()

    count = 0
    target = random.randint(1, 20)

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    while(True):
        print("Take a guess.")
        guess = int(input())
        count+=1

        if guess < target:
            print("Your guess is too low.")
        if guess > target:
            print("Your guess is too high.")
        if guess == target:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break
        

GuessNum_Game()






















        

        


