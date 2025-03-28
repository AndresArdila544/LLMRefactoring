import sys

H, W = map(int, sys.stdin.readline().split())
if H == 0 and W == 0:
    exit()

idx = f'#{W*"."}#\n'
con = ""
if W > 2:
    con = (f"#{'.'*(W-2)}#\n") * (H - 2)
if H >= 2:
    con += idx

print(idx + con)