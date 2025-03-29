```python
a = int(input())
print("{}:{:02d}:{:02d}".format(*divmod(a, 360*60)))