def scores(card1, card2):
    if card1 == card2:
        return (1, 1)
    elif card1 > card2:
        return (3, 0)
    else:
        return (0, 3)


def run():
    c = int(input())
    taro, hanako = 0, 0
    for i in range(c):
        pt, ph = scores(*(input().split())).split()
        taro += int(pt)
        hanako += int(ph)
    print(taro, hanako) 

if __name__ == '__main__':
    run()