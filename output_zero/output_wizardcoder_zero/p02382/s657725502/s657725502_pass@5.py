def stats(n):
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = []
    for i in range(n):
        diff = abs(X[i] - Y[i])
        s1 += diff
        s2 += diff ** 2
        s3 += diff ** 3
        s4.append(diff)
        
    return (s1, math.sqrt(s2), math.pow(s3, 1/3), max(s4))
    
n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

s1, s2_sqrt, s3_cuberoot, s4_max = stats(n)

print('{:.6f}'.format(s1))
print('{:.6f}'.format(s2_sqrt))
print('{:.6f}'.format(math.pow(s3_cuberoot, 1/3))
print('{:.6f}'.format(s4_max)
```