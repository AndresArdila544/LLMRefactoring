```python
dice = [int(x) for x in input().split()]
move = list(input())
direction_map = {"N": [2,6,3,4,1,5],"S":[5,1,3,4,6,2], "E":[4,2,1,6,5,3], "W":[3,2,6,1,5,4]}

for direction in move:
    dice = [direction_map[direction][x-1] for x in dice]
print(dice[-1]) # print the last element of the new list after all the moves are made.
```