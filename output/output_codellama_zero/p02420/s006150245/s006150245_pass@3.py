while True:
    deck = input()
    if deck == '-':
        break
    m = int(input())
    h = list(map(int, input().split()))
    print(''.join(sorted(deck, key=lambda x:h.index(x))))