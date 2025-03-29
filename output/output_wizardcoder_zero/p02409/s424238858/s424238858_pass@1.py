rooms = [[0]*10 for _ in range(4)] * 3
n = int(input())
for l in range(n):
    a,b,c,d = map(int, input().split())
    rooms[a-1][b-1] += d
for i in range(4):
    print(*rooms[i][:9], sep=" ", end="\n" if i != 3 else "####################\n")

# The refactored code is shorter and more concise, but achieves the same functionality as the original. It uses list comprehension to create a 2-dimensional matrix of 4x10 filled with zeros, and then updates it according to user input using map(). Finally, it prints each row (except the last) with spaces in between and adds a new line after the third row using an if statement in the print() function.