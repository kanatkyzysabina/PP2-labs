import string
for letter in string.ascii_uppercase:
    file_name = letter + '.txt'
    open(file_name, 'w')
