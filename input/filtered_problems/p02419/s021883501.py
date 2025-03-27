W = input().lower()
count = 0
line = []
while True:
    tmp_line = input()
    if tmp_line == "END_OF_TEXT":
        break
    line += tmp_line.lower().split()    
    
for word in line:
    if word == W:
        count += 1
    else:
        pass    
print(count)
