
import re

with open(r'/Users/madina/Desktop/PP2-labs/lab5/text.txt', 'r') as file:
    match_text = file.read()
    pattern = re.compile(r'ab*')
    matches = pattern.findall(match_text, re.I)

    if matches:
            print("Found!")
    else:
            print("None")


