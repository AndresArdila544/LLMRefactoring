while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    idx = '#'*W + '\n'
    con = ""
    if W > 2:
        con = ('#.'*(W-2) + '#\n') * (H-2)
    if H >= 2:
        print(idx, end='')
        print(con, end='')
    else:
        print(idx)