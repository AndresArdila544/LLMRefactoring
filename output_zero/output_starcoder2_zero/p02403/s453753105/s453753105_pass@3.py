"""

# The original version was 71 lines
# The refactored version is 32 lines

def main():
    while True:
        H, W = map(int, input().split())
        
        if H == 0 and W == 0:
            break
        
        for h in range(H):
            print('#' * W)
            
        print()

main()