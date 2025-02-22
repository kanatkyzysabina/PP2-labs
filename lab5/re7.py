import re

with open(r'/Users/madina/Desktop/PP2-labs/lab5/text.txt', 'r') as file:
    match_text = file.read()

matches = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), match_text)

print(matches)
