```python
n = int(input())
taro_count = hana_count = 0
for _ in range(n):
    taro, hana = map(int, input().split())
    if taro > hana:
        taro_count += 3
    elif taro == hana:
        taro_count += 1
        hana_count += 1
    else:
        hana_count += 3
print(taro_count, hana_count)
```