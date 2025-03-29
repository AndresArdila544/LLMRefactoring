```python
counter = 1
while True:
    x = input()
    if x == '0':
        break
    print(f"Case {counter}: {x}")
        counter += 1
``` 
Refactored version:

```python
for i in iter(int, 1):
    x = input()
    if x == '0':
        break
    print(f"Case {i}: {x}")
```