```python
def roll_dice(n): # n = number of dice to roll
    faces = [int(i) for i in input().rstrip().split()]
    return [int(faces[2*n+1]), int(faces[(2*n+1)%6])] if n % 2 == 0 else [int(faces[((n-1)*2 + 3) % 6], int(faces[(n-1)*2+4] % 6)]
    
dice = roll_dice(int(input()) # number of dice to roll
command = input().split()
print(roll_dice(len(command))[0]) if command.count('N') > command.count('S') else roll_dice(len(command))[1]
```

Explanation: 

The program initializes the input values for the dice faces and then determines the answer based on the number of north or south commands in the list of commands. If there are more norths than souths, it prints the face value for the top of the n-th dice (where n is the length of the command list) otherwise it prints the face value for the top of the (n+1)-th dice.

The `roll_dice()` function takes an integer argument `n` and returns a list containing the two values on each side of the die. If `n` is even, it means that we are rolling an odd number of dice and we want to find the top face value of the n-th dice. We use modular arithmetic to get the appropriate faces based on the index of each die's position in the list of input values.

If `n` is odd, then we are rolling an even number of dice and we want to find the top face value of the (n+1)-th dice. We use modular arithmetic again to get the appropriate faces based on the index of each die's position in the list of input values.

If there are no more north commands than south commands, then the answer is simply the top value of the (n+1)-th dice.