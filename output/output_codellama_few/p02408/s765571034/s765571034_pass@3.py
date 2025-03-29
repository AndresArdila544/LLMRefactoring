Here is a more concise and readable version of the original Python program:

n = int(input())
cards = [(m, int(n)) for m, n in input().split()]
for m in 'SHCD':
    for n in range(1, 13 + 1):
        if (m, n) not in cards:
            print(m, n)