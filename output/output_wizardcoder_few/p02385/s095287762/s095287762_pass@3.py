class Dice:
    same_dice_index = ('123456', '135246', '142536', '154326', '214365', '231645', '246135', '263415', '312564', '326154', '351624', '365214', '415263', '421653', '456123', '462513', '513462', '536142', '541632', '564312', '624351', '632541', '645231', '653421')
 
    def __init__(self, num_list):
        self.faces = num_list
 
    def is_same(self, dice):
        for i in Dice.same_dice_index:
            example_faces = [0]*6
            for j in range(6):
                example_faces[int(i) - 1] = self.faces[j]
            if all([example_faces[k] == dice.faces[k] for k in range(6)]):
                return 'Yes'
        return 'No'
 
num_list1, num_list2 = list(map(int, input().split())), list(map(int, input().split()))
dice1, dice2 = Dice(num_list1), Dice(num_list2)
 
ans = dice1.is_same(dice2)
 
print(ans)