import sys

cards = []
for i in range(int(input())):
    cards.append((input().split()))

for m in ['S','H','C','D']:
    for n in range(1, 13+1):
        if (m, n) not in cards:
            print(m, n)