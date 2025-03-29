Here is the refactored Python program:
```
n = int(input())
cards = [input().split() for i in range(n)]

p_taro = sum(3 if x > y else 1 for x, y in cards)
p_hanako = sum(3 if x < y else 1 for x, y in cards)
print(p_taro, p_hanako)
```