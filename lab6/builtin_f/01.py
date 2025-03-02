lst = [2, 3, 4, 5]

it = iter(lst)
product = next(it)

for num in it:
    product = pow(product, 1) * pow(num, 1)

print("Product:", product)
