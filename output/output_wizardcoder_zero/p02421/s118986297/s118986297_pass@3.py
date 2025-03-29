```python
point_t = 0
point_h = 0
n = int(input())
for _ in range(n):
    card_t, card_h = map(int, input().split()) # Use a list comprehension to iterate over the input and split it by whitespace
    if card_t > card_h:
        point_t += 3
    elif card_t < card_h:
        point_h += 3
    else:
        point_t += 1
        point_h += 1
print(point_t, point_h)
```

This code achieves the same functionality as the original program, but is more concise by using a single if-else statement instead of multiple if statements. The map function is also used to split the input and convert it into integers.

By using `elif` instead of two separate if statements for card_t < card_h, we reduce the amount of code needed and make it more readable as well.