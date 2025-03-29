```python
n = int(input())
point_t, point_h = 0, 0
for i in range(n):
    card_t, card_h = input().split()
    if float(card_t) > float(card_h):
        point_t += 3
    elif float(card_t) < float(card_h):
        point_h += 3
    else:
        point_t += 1
        point_h += 1
print(point_t, point_h)
```

Explanation: 

- We can initialize `point_t` and `point_h` variables to zero before the loop since they are updated inside it.
- Since both conditions for the if statement are mutually exclusive, we only need one `if-elif-else` block instead of three separate ones.
- The `float()` function can be applied directly on input values without creating new variables.