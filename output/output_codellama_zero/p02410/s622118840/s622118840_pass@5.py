import numpy as np
def func():
    n,m=map(int,input().split())
    matrix = np.array([[int(i) for i in input().split()] for _ in range(n)])
    vector = np.array([int(i) for i in input().split()])
    result=np.dot(matrix,vector)
    print(*result,sep='\n')
func()