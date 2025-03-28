card_lst = []
card_type = ['S', 'H', 'C', 'D']
for tp in card_type:
    for i in range(13):
        card_lst.append('{0} {1}'.format(tp, i+1))
cnt = int(input())
for _ in range(cnt):
    card_lst.remove(input())
print('\n'.join(card_lst)