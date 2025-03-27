Here is a refactored version of the Python program:

card_lst = []
card_type = ['S', 'H', 'C', 'D']
for tp in card_type:
    for i in range(13):
        card_lst.append(tp + ' ' + str(i + 1))
cnt = int(input())
for _ in range(cnt):
   card_lst.remove(input())
[print(c) for c in card_lst]