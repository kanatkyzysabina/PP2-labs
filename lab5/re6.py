import re

with open(r'/Users/madina/Desktop/PP2-labs/lab5/text.txt', 'r') as file:
    match_text = file.read()
    


pattern = re.compile(r'[ ,.]')

matches = re.sub(pattern, ':', match_text)

print(matches)
    