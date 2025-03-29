n=int(input())
dice = Dice(*map(int, input().split()))
for _ in range(n-1):
    s='SSSWEEE'
    w='YYYY'
    ans='Yes'
    for u in range(n-1):
        for t in range(u+1,n):
            if dice.a[t]==dice.a:
                ans='No'
                break
            else:
                dice.roll(*dice.direction[''.join([s[::2][t%4],w[::2][t%4]])), t)
        else:
            continue
        break
    else:
        continue
        break
print(ans)