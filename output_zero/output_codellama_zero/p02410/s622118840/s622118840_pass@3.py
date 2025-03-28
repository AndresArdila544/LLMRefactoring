# coding: utf-8

from numpy import array, dot

def func():
    try:
        (n, m) = tuple(int(num) for num in input().rstrip().split(" ") if num.isdigit())
        matrix = array([[int(num) for num in input().rstrip().split(" ")] for i in range(n)])
        vector = array([int(input().rstrip()) for i in range(m)])
    except:
        return -1

    result = dot(matrix, vector)
    for num in result:
        print(num)