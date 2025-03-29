def lessthen(a, b):
    return a < b

a, b, c = map(int, input().split())
if lessthen(a, b) and lessthen(b, c):
    print('Yes')
else:
    print('No')