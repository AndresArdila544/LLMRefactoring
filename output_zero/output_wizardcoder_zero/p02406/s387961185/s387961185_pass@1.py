a = int(input())
print(*[x for x in range(1, a+1) if (x % 3 == 0 or '3' in str(x)), end=' ')