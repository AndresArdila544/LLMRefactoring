# coding: utf-8
num = int(input())
print(*[i for i in range(1, num+1) if i % 3 == 0 or '3' in str(i)], sep=' ')