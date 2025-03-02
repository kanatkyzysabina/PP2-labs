import os
my_path = '/Users/madina/Desktop/PP2-labs/lab4'

existence = os.access(my_path, os.F_OK)
readabillity = os.access(my_path, os.R_OK)
writeabillity = os.access(my_path, os.W_OK)
executeabillity = os.access(my_path, os.X_OK)

print('Path: ', my_path)

print('Does this path exists?')
if existence:
    print('Yes')
else:
    print('No')


print('Is it possible to read it?')
if readabillity:
    print('Yes')
else:
    print('No')


print('Is it possible to write in it?')
if writeabillity:
    print('Yes')
else:
    print('No')


print('Is it possible to execute it?')
if executeabillity:
    print('Yes')
else:
    print('No')

