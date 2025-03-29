```python
while True:
    N = list(map(int, input().split()))
    if sum(N) == 0:
        break #finish
    else:
        for i in range(N[0]):# H
            print("#"*(N[1])
            if i not in (0, N[0]-1):
                print(".")*(N[1]-2)+"#"
        print()
```