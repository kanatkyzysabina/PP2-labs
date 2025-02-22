import re
with open(r'/Users/madina/Desktop/PP2-labs/lab5/text.txt', 'r') as file:
    match_text = file.read()

def insert_spaces(text):
    return re.sub(r'(?<!\s)(?=[A-Z])', ' ', text).strip()


result = insert_spaces(match_text)
print(result)
