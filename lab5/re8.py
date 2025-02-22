import re

with open(r'/Users/madina/Desktop/PP2-labs/lab5/text.txt', 'r') as file:
    match_text = file.read()


matches = re.split(r'(?=[A-Z])', match_text)

print(matches)
