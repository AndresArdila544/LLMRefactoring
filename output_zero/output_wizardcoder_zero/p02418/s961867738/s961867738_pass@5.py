s = input()
p = input()
if all(i in s for i in p):
    print("Yes") if len(set(p) == 1 or (len(p) <= len(s) and all((p[j] == s[(i + j) % len(s)] for i, p in enumerate(p))) else "No")
"""Refactored version of the code with fewer lines and improved readability. The 'any' function is used to reduce the number of loops and increase readability. The enumeration technique is also utilized to improve the code.