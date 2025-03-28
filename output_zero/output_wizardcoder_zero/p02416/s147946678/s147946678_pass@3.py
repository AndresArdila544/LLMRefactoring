```python
def sum_digits(n):
    return sum(int(d) for d in str(n))
while True:
  x = input()
  if x == '0':
    break
  print(sum_digits(x)) 
```