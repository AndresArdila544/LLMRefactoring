import sys
input = sys.stdin.readline

# initialize a list of lists to store the values
rooms = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]

# get number of test cases from input
n = int(input())

# loop through each test case
for l in range(n):
    # get values a, b, c, and d from input
    a,b,c,d = map(int, input().split())
    
    # update the value at index (a-1, b-1, c-1) in the 3D list
    rooms[a-1][b-1][c-1] += d

# print the 2D list of lists, with each element separated by a space and a newline character after each row
for i in range(4):
    for j in range(3):
        for k in range(10):
            print(rooms[i][j][k], end="")
            if k != 9:
                print(" ", end="")
        if i != 3 or j !=2:
            print()
    if i != 3:
        print("####################")