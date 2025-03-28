```python
n = int(input())
number = [str(i) for i in range(1, n+1 if str(i).find("3") != -1 or i % 3 == 0 else None] 
print(" ".join(filter(None, number))