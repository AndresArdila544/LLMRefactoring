n = input().split()
count = int(input())
dice = Dice(*map(int, n))
for _ in range(count):
    buf = input().split()
    dice.rotate("E", int(buf[0]))
    dice.rotate("S", int(buf[1]))
    print(dice.south)