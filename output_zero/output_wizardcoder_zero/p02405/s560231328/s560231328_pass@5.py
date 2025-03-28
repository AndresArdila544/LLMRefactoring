def draw_checkerboard():
    while True:
        nums = map(int, input().split())
        H, W = nums[0], nums[1]
        if H == 0:
            break
        so, se = ".", "#"
        for i in range(H):
            for j in range(W):
                print("." * (j & 1) + "#" + "." * (~j & 1), end="")
            print()
            if i & 1:
                so, se = se, so
        
draw_checkerboard()