user_input = input("Enter tuple elements separated by spaces: ").split()

def convert(value):
    if value.isdigit():
        return int(value)  
    elif value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    return value

my_tuple = tuple(map(convert, user_input))
result = all(my_tuple)

print("Tuple:", my_tuple)
print("Are all elements True?", result)
