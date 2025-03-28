Here is my solution: 

n = int(raw_input())
a = map(int, raw_input().split())
while n > 0:
    print a[n - 1], n -= 1