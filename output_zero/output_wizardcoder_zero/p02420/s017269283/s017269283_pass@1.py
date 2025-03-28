```python
alp = input()
while alp != '-':
    m = int(input())
    for i in range(m):
        h = int(input())
        alp = alp[h:] + alp[:h]
    print(alp)