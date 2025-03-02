import time

number = float(input('Enter number: '))
milliseconds = float(input('Enter time in milliseconds: '))

time.sleep(milliseconds/1000)

sqrt_num = pow(number, 0.5)
print(f"Square root of {number} after {milliseconds} miliseconds is {sqrt_num}")
