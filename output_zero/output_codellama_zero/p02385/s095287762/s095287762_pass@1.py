class Dice:
    def __init__(self, faces):
        self.faces = faces
    
    @staticmethod
    def is_same(dice1, dice2):
        for i in Dice.same_dice_index:
            example_faces = []
            for j in i:
                example_faces.append(dice1.faces[int(j) - 1])
            if example_faces == dice2.faces:
                return 'Yes'
        return 'No'
    
num_list1 = list(map(int, input().split()))
num_list2 = list(map(int, input().split()))
 
dice1 = Dice(num_list1)
dice2 = Dice(num_list2)
 
ans = Dice.is_same(dice1, dice2)
 
print(ans)