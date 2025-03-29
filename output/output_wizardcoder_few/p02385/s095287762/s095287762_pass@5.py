```python
class Dice:
    same_dice_index = ['123456', '135246', '142536', '154326', 
                     '214365', '231645', '246135', '263415',
                    '312564', '326154', '351624', '365214', 
                     '415263', '421653', '456123', '462513',
                    '513462', '536142', '541632', '564312',
                     '624351', '632541', '645231', '653421']
  
    def __init__(self, num_list):
        self.faces = num_list
      
    def is_same(self, dice):
        for i in Dice.same_dice_index:
            example_faces = []
            for j in i:
                example_faces.append(str(self.faces[int(j) - 1])
            if ''.join(example_faces) == ''.join(dice.faces):
                return True
        return False
  
num_list1 = list(map(int, input().split()))
num_list2 = list(map(int, input().split()))
  
ans = Dice(num_list1).is_same(Dice(num_list2))
  
print('Yes' if ans else 'No')
```