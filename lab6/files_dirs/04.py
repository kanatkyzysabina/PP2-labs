file_name = "lyrics.txt"
count = 0
with open(file_name) as file:
    for line in file:
        count += 1

print("Number of lines in file:", count)