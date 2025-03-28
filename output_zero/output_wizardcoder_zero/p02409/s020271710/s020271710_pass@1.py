```python
n = int(input())
listA = [list(map(int, input().split())) for i in range(n)]  # Taking input as list of lists

for line_num, building in enumerate(listA):
    floor_num = (line_num // 4) + 1  # Calculating floor number
    room_num = (line_num % 4) * 3 + ((building[0] - 1) % 10)
    building[(floor_num-1)] [room_num] += building[3]  # Incrementing the value in the corresponding floor and room for each input line

for floor_num, building in enumerate(listA[:4]):
    print(" ".join([str(val) for val in building]))
    if floor_num < 2:
        print("#" * 20)
```

This code will have the same functionality as the original code, but with lesser lines and more concise code structure. The input is taken as a list of lists using `listA = [list(map(int, input().split()) for i in range(n)]`, which makes it easier to iterate over the data.