```python
while True:
    m,f,r = list(map(int,input().split()))
    if m==-1 and f==-1 and r==-1:
        break
    elif (m+f<30) or (m==-1 or f==-1):
        print("F")
    elif 50>=r>=(m+f<50):
        print("D")
    elif m+f<80:
        print("B")
    else:
        print("A")
```

In the original code, it was checking for the conditions separately which is not necessary. In the refactored version, we can combine them using logical operators and conditions to reduce the complexity and make it more concise.