a = list(map(int, input().split()))
print('a < b' if a[0] < a[1] else 'a > b' if a[0] > a[1] else 'a == b')