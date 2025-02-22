import re

with open(r'/Users/madina/Desktop/PP2-labs/lab5/text.txt', 'r') as file:
    match_text = file.read()
    pattern = re.compile(r'[a-z]+(?:_[a-z]+)+')
    matches = pattern.findall(match_text)
    if matches:
        print(matches)
    else:
        print('None')
    