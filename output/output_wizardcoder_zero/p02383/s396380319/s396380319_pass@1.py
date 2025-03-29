```python
dice = [int(input()) for _ in range(6)] #initialize dice with 6 elements
move_list = input().split() #store moves in a list
for direction in move_list:
    index_dict = {"N":[2,6,3,4,1],"S":[5,1,3,4,6], "E":[4,2,1,6,5],"W":[3,2,6,1,5]}
    dice = [index_dict[direction][d-1] for d in range(len(move_list)]
```