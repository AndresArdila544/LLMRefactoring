def main():
    s = input()
    q = int(input())
    for _ in range(q):
        meth, a, b, *p = input().split()
        if meth == "print":
            print(s[int(a) : int(b) + 1])
        elif meth == "reverse":
            s = s[:int(a)] + s[int(a):int(b)+1][::-1] + s[int(b)+1:]
        elif meth == "replace":
            s = s[:int(a)] + "".join(p) + s[int(b)+1:]