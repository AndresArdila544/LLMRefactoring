import sys
input = sys.stdin.readline

cards = []
patterns = ['S', 'H', 'C', 'D']

n = int(input())
for p in patterns:
	for i in range(1, 13+1):
		cards.append(p + ' ' + str(i))

while n>0:
	cards.remove(input().strip())
	n-=1

for c in cards:
	print(c)