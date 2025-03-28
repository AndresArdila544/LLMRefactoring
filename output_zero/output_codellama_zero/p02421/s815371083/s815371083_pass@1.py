```
import math
N = int(input())
AP=0
BP=0
for i in range(N):
    A, B = input().split()
    if A==B:
        AP+=1
        BP+=1
    else:
        X = math.max(len(A), len(B))
        for j in range(X):
            if ord(A[j]) > ord(B[j]):
                AP += 3
                break
            elif ord(B[j]) > ord(A[j]):
                BP += 3
                break
print(AP, BP)
```
This code is equivalent to the original code in terms of its functionality. However, it is more concise and easier to read due to fewer lines and improved formatting.