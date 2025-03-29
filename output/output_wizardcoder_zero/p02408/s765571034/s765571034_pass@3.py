n=int(input())
suits = ['S', 'H', 'D']
for m in suits:
    for n in range(1, 13+1):
        if (m,n) not in [(x[0], x[1]) for x in cards]:
            print(m, n)