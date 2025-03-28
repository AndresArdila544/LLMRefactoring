```
n = int(input())
cards = [input().split() for i in range(n)]
p_taro = sum([3 if cards[i][0] > cards[i][1] else 1 for i in range(n)])
p_hanako = sum([3 if cards[i][0] < cards[i][1] else 1 for i in range(n)])
print(p_taro, p_hanako)
```