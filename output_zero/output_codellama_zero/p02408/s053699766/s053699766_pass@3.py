card_lst = [ f"{tp} {i+1}" for tp in ['S', 'H', 'C', 'D'] for i in range(13)]
cnt = int(input())
card_lst = card_lst[:-cnt]
[print(c) for c in card_lst]