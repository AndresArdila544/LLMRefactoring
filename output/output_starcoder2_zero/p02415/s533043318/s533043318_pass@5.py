The following is the original program:

def maketrans():
    lower = "abcdefghijklmnopqrstuvwxyz"
    trans = {}
    for i in range(len(lower)):
        trans[lower[i]] = str.upper(lower[i])
        trans[str.upper(lower[i])] = lower[i]
    return trans
s = input()
print(s.translate(maketrans()))