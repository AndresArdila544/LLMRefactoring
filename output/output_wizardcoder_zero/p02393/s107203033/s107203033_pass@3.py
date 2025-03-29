num = input().split()
print(' '.join(map(str, sorted([int(i) for i in num])) + [" "])[0:-1])