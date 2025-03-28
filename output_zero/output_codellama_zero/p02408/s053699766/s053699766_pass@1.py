Here is the refactored Python program with fewer lines and improved readability:

card_lst = []
card_type = ['S', 'H', 'C', 'D']
for tp in card_type:
    for i in range(13):
        card_lst.append(tp + ' ' + str(i + 1))
cnt = int(input())
card_lst.sort()
for c in card_lst[:-cnt]:
   print(c)