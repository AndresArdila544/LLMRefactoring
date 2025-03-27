"""

# Original Python code
# s = input()
# p = input()
# s += s
# if p in s:
    # print('Yes')
# else:
    # print('No')
    
# Refactored version of the Python code
s = input()
p = input()
if p in (s + s):
    print("Yes")
else:
    print("No")