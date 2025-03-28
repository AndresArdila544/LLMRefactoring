H,W=map(int,input().split())
while (W>0 and H>0):
    for i in range(H):
        print(''.join(['.' if j%2 else '#'*(i%2==0) or not (j%2) else '#'*(not (i%2)) for j in range(W)]), end='\n')
print()
H,W=map(int,input().split())