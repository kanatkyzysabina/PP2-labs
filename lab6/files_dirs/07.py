copy = 'copylyrics.file'
orig = 'lyrics.txt'

with open(orig, 'r') as source, open(copy, 'w') as aim:
    for line in source:
        aim.write(line)

    