# coding: utf-8
# Here your code !

from numpy import array, dot

def func():
    try:
        (n,m) = tuple( [ int(num) for num in input().rstrip().split(" ") ] )
        matrix = array( [ [int(num) for num in input().rstrip().split(" ")] for i in range(n) ] )
        vector = array( [ int( input().rstrip() ) for i in range(m) ] )
    except:
        return inputError()

    result = dot(matrix,vector)
    for num in result:
        print(num)
    
def inputError():
    print("input error")
    return -1

func()