import sys

for _ in range(int(sys.stdin.readline())):
    h, w = map(int, sys.stdin.readline().split())
    if not (h and w): break
    border = "#" * w + "\n"
    inner_border = ("#." * (w - 2) + "#\n") * (h - 3)
    result = border + inner_border + border
    print(result)