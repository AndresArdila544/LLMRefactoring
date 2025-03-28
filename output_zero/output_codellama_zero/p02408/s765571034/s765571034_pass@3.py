cards = []
for i in range(int(input())):
    cards.append(tuple((i.split() for i in input().split())[1]))
    
print(*[item for item in ['S', 'H', 'C', 'D'] if item not in cards], sep='\n')