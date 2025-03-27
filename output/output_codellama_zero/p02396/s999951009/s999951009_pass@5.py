a = []
while True:
    tmp = int(input())
    if tmp == 0: break
    a.append(tmp)
for index, value in enumerate(a,1):
    print(f'Case {index}: {value}')