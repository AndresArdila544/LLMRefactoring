Here is a refactored version of your original Python program with cleaner syntax:

W, H, x, y, r = map(int, input().split())
print("Yes" if 0 <= x + r <= W and 0 <= y + r <= H and -r <= x - r < W and -r <= y - r < H else "No")