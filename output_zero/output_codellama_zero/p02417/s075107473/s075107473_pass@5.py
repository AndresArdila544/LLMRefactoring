Here is a refactored version of the Python program:

# coding: utf-8
# Your code here!

while True:
    try:
        n = input()
        m = str(n).lower()
        t += m
    except:
        break
for i in range (97,123):
    y[i-97] = sum(c == chr(i) for c in t)
print(*(f'{chr(i)} : {y[i-97]}' for i in range(97,123)), sep='\n')