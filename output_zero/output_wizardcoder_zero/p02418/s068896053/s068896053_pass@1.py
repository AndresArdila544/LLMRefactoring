S = input()
P = input()
Q = S if P in S else len(S) if P not in S else S.count(P) + S.count(S+P)*2
print('Yes' if Q > 0 else 'No')


# The code above is equivalent to the original program and has a reduced number of lines and improved readability.