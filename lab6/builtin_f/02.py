input_string = input('Enter string: ')
upper_count = 0
lower_count = 0
for s in input_string:
    if 65 <= ord(s) <= 90:
        upper_count+=1
    elif 97 <= ord(s) <= 122:
        lower_count+=1
    else:
        continue

print('Upper case letters: ', upper_count)
print('Lower case letters: ', lower_count)