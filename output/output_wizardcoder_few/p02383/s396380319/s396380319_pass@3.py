refactored_code = """
dice = [int(i) for i in input().split()]
move = [i for i in input()]
dire = {"N": [2,6,3,4,1,5,"S":[5,1,3,4,6],"E":[4,2,1,6,5],"W":[3,2,6,1,4]} # Refactored code with less lines and improved readability
em = []
for i in range(len(move)):
    em = dice[:]
    for j in range(len(dice):
        em[j] = dice[dire[move[i][j-1]]-1] if move[i] in "NS" else dice[dire[move[i][j-1]]]-3 if move[i] == "EW" else dice[dire[move[i][j-1]]+2
    else:
        del dice[:]
        dice.extend(em)
print(dice[0])
"""

# Explanation: 
# We first take the input as integers and store them in a list called 'dice'. Then we use a dictionary called 'dire' which stores all the possible positions that the die can move from.
# In each iteration of the loop, we create a new list 'em' and copy the values of 'dice' into it. Then we update 'em' based on the value of the move entered by the user. 
# The if-else statement checks whether the input is either 'N', 'S', 'E', or 'W'. If the input is in those directions, we replace the values with their respective new positions in the dice list using their keys in the dictionary.
# If the input is not any of the above, we add 2 to the original value if it's 'E' and subtract 3 from it if it's 'W'. Finally, we print the final value of dice[0] which should be the starting position after all the moves are made.
"""

refactored_code = """
dice = [int(i) for i in input().split()]
move = [i for i in input()]
dire = {"N": (2,6,3,4,1,"S":(5,1,3,4,6),"E":(4,2,1,6),"W":(3,2,6,1)} # Refactored code with less lines and improved readability
em = []
for i in range(len(move)):
    em = dice[:]
    for j in range(len(dice):
        if move[i] in "NS":
            em[j] = dire[move[i][j-1][0]
        elif move[i] == "EW":
            em[j] += 2 if move[i] == "E"
        else:
            em[j] -= 3
    else:
        del dice[:]
        dice.extend(em)
print(dice[0])
"""