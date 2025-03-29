```python
n = int(input())
x = list(map(int, input().split()))
min_num = min(x)
max_num = max(x)
total = sum(x)
print("{} {} {}".format(min_num, max_num))