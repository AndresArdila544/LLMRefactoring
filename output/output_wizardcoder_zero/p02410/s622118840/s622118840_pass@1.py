import numpy as np

def main():
    try:
        n, m = map(int, input().split())
        matrix = np.array([list(map(int, input().split())) for i in range(n)])
        vector = np.array(list(map(int, input().split()))
        
        if len(vector) != m:
            return "Input error"
            
        result = np.dot(matrix, vector)
        print(*result)
    except:
        return "Input error"