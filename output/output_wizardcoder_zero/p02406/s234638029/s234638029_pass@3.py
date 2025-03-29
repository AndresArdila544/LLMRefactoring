```python
num = int(input())
print(*[str(i) if i % 3 == 0 and "3" not in str(i) else "" for i in range(1, num+1)])
```
```python
num = int(input())
for i in range(1, num+1):
    print(str(i), end=" ") if i % 3 and "3" not in str(i) else "", end=""
print()
```