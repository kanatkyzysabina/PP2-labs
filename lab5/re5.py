import re

with open(r'/Users/madina/Desktop/PP2-labs/lab5/text.txt', 'r') as file:
    match_text = file.read()
    


pattern = re.compile(r'a.*?b')

matches = re.findall(pattern, match_text)

if matches:
    print(matches)
    print('Found!')
else:
    print('None')
    