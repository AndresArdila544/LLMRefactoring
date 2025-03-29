n = int(input())
print(*(str(i) for i in range(1, n+1) if not (i % 3 or '3' in str(i)), sep='')