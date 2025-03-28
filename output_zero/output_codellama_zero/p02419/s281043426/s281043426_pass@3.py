import sys
W=input()
T=sys.stdin.read().split()
count=0
for s in T:
    if s=='END_OF_TEXT':break
    target=s.lower()
    if target == W:
        count += 1
print(count)