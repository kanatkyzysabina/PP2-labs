import math

#1
def convert_degree(d):
    radian = d * (math.pi/180)
    return radian

degree = float(input("Enter degree: "))
radian = convert_degree(degree)
print(f"Degree in radian: {radian:.6f}")


#2
height = float(input("\nHeight of trapezoid: "))
base1 = float(input("Base 1 of trapezoid: "))
base2 = float(input("Base 2 of trapezoid: "))

area = ((base1+base2)/2) * height
print(f"The area of the trapezoid is: {area}")

#3
n = int(input("\nPrint number of sides: "))
s = float(input("Print the length of a side: "))

area = (n * (s**2)) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is: {area:.0f}")

#4
base = float(input("\nPrint length of the base: "))
height = float(input("Print height of the parallelogram: "))

area = base*height
print(f"The area of the parallelogram is: {area:.1f}")


