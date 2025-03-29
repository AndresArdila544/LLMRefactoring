def print_pattern(H, W):
    idx = '#'*W + '\n'
    con = '' if H == 1 else ('#.'*(W-2) + '#\n') * (H-2)
    if H >= 2: con += idx 
    print(idx + con)

while True:
    H, W = map(int,input().split())
    if H==0 and W==0: break
    print_pattern(H,W)