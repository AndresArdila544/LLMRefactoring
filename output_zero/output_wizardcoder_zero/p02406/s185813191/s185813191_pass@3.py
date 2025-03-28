n = int(input())
print(*[i for i in range(1, n+1) if (not i%3 and '3' in str(i)) or i%3], end='')