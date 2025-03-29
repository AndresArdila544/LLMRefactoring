n = int(input())
while n > 0:
    s = list(map(int, input().split()))
    m = sum(s)/len(s)
    print(sum([math.sqrt((x - m)**2 for x in s))/len(s), end=' ')
    n -= 1
print()