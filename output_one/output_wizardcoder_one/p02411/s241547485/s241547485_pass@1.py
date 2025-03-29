```python
while True:
    m,f,r=list(map(int,input().split()))
    if all(x==-1 for x in (m, f, r): 
        break
    elif any((m+f<30) or m==-1) and not r==50: 
        print("F")
    elif 50<=r<65 and m+f<50: 
        print("D")
    elif all(x>49 for x in (m, f): 
        print("C")
    elif m+f<80: 
        print("B")
    else: 
        print("A")