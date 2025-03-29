W = input().lower()
count = 0
line = []
while True:
    tmp_line = input()
    if tmp_line == "END_OF_TEXT":
        break
    line += [word.lower() for word in tmp_line.split()] 
print(len([word for word in line if word == W]))