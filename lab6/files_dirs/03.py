import os

my_path = '/Users/madina/Desktop/PP2-labs/lab4'
print('Path: ', my_path)

print('Does this path exists?:')

if os.path.exists(my_path):
    print('Yes it exists')
    entries = os.scandir(my_path)
    for entry in entries:
        if entry.is_file():
            print('Filename portion:', entry.name)
            print('Directory portion: ', os.path.dirname(entry.path))
else:
    print('No such path does not exists')
