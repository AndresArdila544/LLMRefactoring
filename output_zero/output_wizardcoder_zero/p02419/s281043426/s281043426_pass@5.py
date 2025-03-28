import sys

W = input()
T = input().split()
count = 0
for i in range(len(T)):
    if T[i] == "END_OF_TEXT":
        break
    target = T[i].lower()
    if W.lower() == target:
        count += 1
print(count)