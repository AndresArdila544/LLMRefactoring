W = input().lower()
line = []
while True:
    tmp_line = input()
    if tmp_line == "END_OF_TEXT":
        break
    line += tmp_line.lower().split()    
count = sum(1 for word in line if word == W)