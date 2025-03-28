```python
while True:
    num = input()
    if(num == "0"): break
    print(sum(int(digit) for digit in num))
```