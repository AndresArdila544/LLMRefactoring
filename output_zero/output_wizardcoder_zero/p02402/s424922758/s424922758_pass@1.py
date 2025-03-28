```python
n = int(input())
table = list(map(int, input().split()))
print(*sorted(table)[:2], sum(table))