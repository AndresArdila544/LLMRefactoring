```python
def main():
    while True:
        n = int(input())
        if not n:
            break
        else:
            b = list(map(int, input().split()))
            ave = sum(b) / n
            A = [(ave - i)**2 for i in b]
            p = math.sqrt(sum(A)/n)
            print("{:.8f}".format(p))
            A.clear()
```