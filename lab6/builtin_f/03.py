input_string = input('Enter string: ')

reverse_string = reversed(input_string)
rev_list = list(reverse_string)


is_palindrome = False
for i in range(len(input_string)):
    if input_string[i] == rev_list[i]:
        is_palindrome = True
    else:
        is_palindrome = False
        break

if is_palindrome:
    print(f'String {input_string} is palindrome!')
else:
    print(f'String {input_string} is NOT a palindrome!')
    