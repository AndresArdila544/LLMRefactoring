card_lst = []
card_type = ['S', 'H', 'C', 'D']
#make table
for tp in card_type:
    for i in range(13):
        card_lst.append(tp + ' ' + str(i + 1))

#remove
cnt = int(input())
for i in range(cnt):
   card_lst.remove(input())

[print(c) for c in card_lst]
