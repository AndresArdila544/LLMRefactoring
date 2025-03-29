def print_hourglass(N):
    for i in range(N[0] - 1): # H lines (top and bottom)
        if not i == N[0] - 1: # top line
            print("#", end="")
            for j in range(N[1]-2): # middle horizontal line with spaces except first and last
                print(" ", end="")
            print("#")
    for i in range(N[1]-1): # N[0] - 2 rows of "## #" with spaces between
        if not i == 0: # skip the first and last row
            print("#", end="")
            for j in range(N[1]-1):
                print(" ", end="")
            print("#")
    print("\n", end="")
    
# input N as a list of two integers separated by spaces
N = list(map(int,input().split()))