class Dice:
    def __init__(self, num_list):
        self.faces = [num for num in num_list]
 
    def is_same(self, other_dice):
        return 'Yes' if all(a == b for a,b in zip(self.faces, other_dice.faces)) else 'No'
 
num_list1 = list(map(int, input().split()))
num_list2 = list(map(int, input().split()))
 
dice1 = Dice(num_list1)
dice2 = Dice(num_list2)
 
print(dice1.is_same(dice2))