#1- - - - -
class StringActions:
  def __init__(self):
    self.inputS = ""

  def getString(self):
    self.inputS = input("Print any word: ")

  def printString(self):
    print(self.inputS.upper())

string1 = StringActions()

string1.getString()
string1.printString()


#2- - - - -

class Shape:
    def __init__(self):
        self.area = 0

    def Area(self):
        print(f"Area of the shape is {self.area}")


class Square(Shape):
    def __init__(self, length):
        self.shape = "Square"
        self.length = length

        super().__init__()
        self.area = self.length * self.length

    def Area(self):
        print(f"Area of the {self.shape} is {self.area}")



square1 = Square(4)
square1.Area()


shape1 = Shape()
shape1.Area()

#3- - - - - 

class Rectangle(Shape):
   def __init__(self, length, width):
      self.shape = "Rectangle"
      self.length = length
      self.width = width
      super().__init__()
      self.area = 0
   def CalcArea(self):
    self.area = self.length * self.width
    print(f"Area of the {self.shape} = {self.area}")

rec1 = Rectangle(6, 4)
rec1.CalcArea()

#4- - - - -
import math

print("\n")
      

class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def show(self):
      print(f"Point: ({self.x}, {self.y})")

   def move(self, newX, newY):
      self.x = newX
      self.y = newY

   def distance(self, another_point):
      distance = math.sqrt((another_point.x - self.x)**2 + (another_point.y - self.y)**2)
      print(f"Distance between ({self.x}, {self.y}) and ({another_point.x}, {another_point.y}) is {distance}")


p1 = Point(2, 6)
p2 = Point(3, 8)

p1.show()
p2.show()

p1.move(6, 10)

p1.distance(p2)


#5- - - - -


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" {amount}$ were deposited. Your new balance: {self.balance}$")
        else:
            print("Deposit amount should be positive!!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied.")
        elif amount > 0:
            self.balance -= amount
            print(f" {amount}$ were withdrew. New balance: {self.balance}$")
        else:
            print("Withdrawal amount should be positive!!")
        

account1 = BankAccount("Tamilana", 2500)

print("\n")
account1.deposit(500)
account1.deposit(-200)


account1.withdraw(500)
account1.withdraw(2000)
account1.withdraw(600)  
account1.withdraw(-20) 



#6- - - - - 

isPrime = lambda x: x > 1 and all(x % i != 0 for i in range(2, x))

n = input("\nEnter numbers for a list: ")

numbers = list(map(int, n.split()))

primeList = list(filter(isPrime, numbers))

print(f"Prime numbers: {primeList}")


      
      