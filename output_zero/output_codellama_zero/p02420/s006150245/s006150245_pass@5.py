while True:
    deck = input()
    if deck == '-':
        break
    m = int(input())
    h = [int(x) for x in input().split()]
    print("".join(sorted(deck, key=lambda x: -ord(x))[i:] + sorted(deck, key=lambda x: -ord(x))[:i] for i in h)))