```python
class Dice:
    same_dice_index = ('123456', '135246', '142536', '154326', 
                   '214365', '231645', '246135', '263415', 
                   '312564', '326154', '351624', '365214',
                   '415263', '421653', '456123', '462513',
                   '513462', '536142', '541632', '564312',
                   '624351', '632541', '645231', '653421')
    def __init__(self, num_list):
        self.faces = num_list
  
    def is_same(self, dice):
        for i in Dice.same_dice_index:
            example_faces = []
            for j in i:
                example_faces.append(str(j))
            if ''.join(map(str, self.faces)) == ''.join(example_faces):
                return 'Yes'
        return 'No'
  
num_list1 = list(input().split())
num_list2 = list(input().split())
  
dice1 = Dice(num_list1)
dice2 = Dice(num_list2)
  
ans = dice1.is_same(dice2)
  
print(ans)
```