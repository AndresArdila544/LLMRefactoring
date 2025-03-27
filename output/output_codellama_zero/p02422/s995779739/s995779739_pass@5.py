def main():
    S = input()
    q = int(input())

    for i in range(q):
        order = list(input().split())
        if order[0] == "replace":
            a, b = map(int, order[1:3])
            S = REPLACE(S, order[3], a, b)
        elif order[0] == "reverse":
            a, b = map(int, order[1:3])
            S = REVERSE(S, a, b)
        else:
            a, b = map(int, order[1:3])
            PRINT(S, a, b)
    return S

def PRINT(S, a, b):
    print(S[a:b+1])

def REPLACE(S, T, a, b):
    return S[:a] + T + S[b+1:]

def REVERSE(S, a, b):
    tmp = S[a:b+1]
    return S[:a] + tmp[::-1] + S[b+1:]

if __name__ == "__main__":
    main()