```
dice = list(map(int, input().split()))
move = input()
dire = {"N": [2, 6, 3, 4, 1, 5], "S": [5, 1, 3, 4, 6, 2], "E": [4, 2, 1, 6, 5, 3], "W": [3, 2, 6, 1, 5, 4]}
dice = list(map(lambda i: dice[dire[move[i]][i]-1], range(len(move))))
print(dice[0])
```