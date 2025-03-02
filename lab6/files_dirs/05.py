new_list = ['hello', ',', 'world', '!']

file_name = 'text.txt'
with open(file_name, 'w') as file:
    for n in new_list:
        file.write(n)
        
