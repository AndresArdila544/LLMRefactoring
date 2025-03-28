a = []
while True:
    try:
        a.append(int(input()))
    except ValueError:
        break
for index, value in enumerate(a, 1):
    print('Case', index, ':', value)