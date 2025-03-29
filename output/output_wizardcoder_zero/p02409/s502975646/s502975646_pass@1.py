buildings = [[[0]*10 for _ in range(3)] for _ in range(4)] # This creates a 4x3x10 matrix of zeros with list comprehension
for i in range(informations):
    x, y, z, val = map(int, input().split())
    buildings[x-1][y-1][z-1] += val # updates the value at the given coordinates
for row in buildings:
    for col in row:
        write(' '.join([str(i) for i in col]) + ' ') # prints each inner list with a space separator
        print()
    if row != buildings[3]: # only print hashes after rows 0-2, and not the last one
        print('#'*21)
        
# Output:
# Input example:
# 5
# 1 1 1 20
# 2 3 4 30
# 2 2 5 40
# 3 1 7 50
# 1 2 8 60
# 3 2 9 70

# Output example:
# 20 
# 0 0 0 #
# 0 0 0 0 #
# 0 0 0 #
# 
# 0 
# 0 
# 
# 30 
# 40 0 
# 0 0 #
# 0 0 #
# 
# 70 
# 0 50 0 
# 0 0 #
# 
# 90 
# 0 0 60 
# 0 0 #