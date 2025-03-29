```python
l=[]
while True:
    l_ = list(map(int, input().split()))
    if l_ == [-1,-1,-1]: break
    l.append(l_)
for i in l:
    if -1 in i or all(i): continue
    elif sum(i) >= 80: print("A")
    elif 65 <= sum(i) < 80: print("B")
    elif 50 <= sum(i) < 65 and not any(map(lambda x: x>=50, i[2:]): print("C")
    elif all(map(lambda x: x<50, i[:-1]) and i[-1] >= 50: print("D")
    else: print("F")
```