W = input().lower()
count = 0
while True:
    tmp_line = input()
    if tmp_line == "END_OF_TEXT":
        break
    for word in tmp_line.lower().split():
        if word == W:
            count += 1
print(count)