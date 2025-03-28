while True:
 n, x = map(int, input().split(' '))
 if n == x ==0: break
 max_a = x // 3
 count = sum((c > b) for a in range(1,n-1) for b in range(a+1, n) for c in range(x - a - b + 1) if c > 0 and c <= n)
 print(count)