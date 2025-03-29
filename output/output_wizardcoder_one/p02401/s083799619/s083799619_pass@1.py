```python
a = input()
while True:
    if '?' in a: 
        break
    print(int(''.join(str(eval(a.split())))
```