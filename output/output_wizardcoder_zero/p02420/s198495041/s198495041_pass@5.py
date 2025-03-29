```python
C = input()
while True:
    C = input() if C == "-" else C + input() * int(input())
print(C)