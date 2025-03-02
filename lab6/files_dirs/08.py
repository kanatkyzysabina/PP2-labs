import os

my_path = '/Users/madina/Desktop/PP2-labs/file_directories'
file_name = 'new.txt'

file_path = os.path.join(my_path, file_name)


print('Path: ', file_path)
        
print('Does this path exists?:')
if os.path.exists(file_path):
    print('Yes it exists')
    print('Do we have access for the path?:')
    if os.access(file_path, os.W_OK):
        print('YES! We have an access for this path')
        os.remove(file_path)
        print('\n- - - - - - - - - - - - - - - - - - -')
        print('\nEnd of the operation. File was successfully deleted! Congratulations.')
    else:
        print('NO!( We dont have an access for this path')
        print('Because of that we cant delete this particular file from path.') 
else:
    print('No such path does not exists. We cant do anything with this path')

