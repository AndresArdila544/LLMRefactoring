a, b = map(int, input().split())
if all(1 <= i <= 100 for i in (a,b): print(f'{a * b} {2*(a+b)}')