#Refactor code to print the matrix
n,m = map(int,input().split())

matrix1  = [list(map(int, input().split())) for i in range(n)]
matrix2 = [list(map(int, input().split())) for i in range(m)]


for row in matrix1:
    for col in row:
        print(col, end=" ")
    
    print()