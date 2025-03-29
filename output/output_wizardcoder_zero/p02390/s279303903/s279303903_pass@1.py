```python
h = int(input()) // 360
m = (int(input()) % 360) // 60
s = input() % 60
print("{}:{}:{}".format(h, m, s)) 
```