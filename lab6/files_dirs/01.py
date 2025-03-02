import os

my_path = '/Users/madina/Desktop/PP2-labs/lab4'
contents = os.listdir(my_path)
print('Path:', my_path)


print('\nDirectories of the path: ')
for content in contents:
    if os.path.isdir(os.path.join(my_path, content)):
        print(content)


print('\nFiles and Directories of the path: ')
for content in contents:
    print(content)


print('\nFiles of the Path: ')
for content in contents:
    if os.path.isfile(os.path.join(my_path, content)):
        print(content)
