x = 0
while True:
    s = input()
    if s != '0':
        x += sum(map(int, s))
    else:
        break
print(x)