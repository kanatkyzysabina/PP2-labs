#1
def squares(start, stop):
    while(start<=stop):
        yield start**2
        start+=1

start = int(input("print start-number: "))
stop = int(input("print stop-number: "))

squares_gen = squares(start, stop)

for s in squares_gen:
    print(s, end=' ')

#2
def even(start, stop):
    while(start<=stop):
        if start%2 == 0:
            yield start
        start+=1

stop = int(input("\n\nprint stop-number: "))
even_gen = even(0, stop)

print(*even_gen, sep=",")

#3
def div_by_34(start, stop):
    while(start <= stop):
        if start % 3 == 0 and start % 4 == 0:
            yield start
        start+=1

stop = int(input("\n\nprint stop-number: "))
div_gen = div_by_34(0, stop)

print(*div_gen, sep = " ")

#4
def power_2(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input("\n\nprint start-number: "))
b = int(input("print stop-number: "))
pow_gen = power_2(a, b)

for p in pow_gen:
    print(p, end=" ")


#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("\n\nprint number: "))
count_gen = countdown(n)

print(*count_gen, sep=" ")
