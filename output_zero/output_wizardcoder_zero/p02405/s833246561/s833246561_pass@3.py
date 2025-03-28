H, W = map(int, input().split())
for i in range(W):
    print("#" * (i%2) + "." * ((1-i%2), end='') + "\n"
         + "." * (1-(i%2)) + "#" * (i%2)
         if i < W else "")