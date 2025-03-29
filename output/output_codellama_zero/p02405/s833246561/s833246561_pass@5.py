Here is a refactored version of the original program that reduces its complexity:

while True:
    H, W = map(int, input().split())
    if not H and not W:
        break
    
    for i in range(0, W):
        row = "#" * (i % 2) + "." * (W - i - 1) * (i % 2)
        print(row)
        
    print()