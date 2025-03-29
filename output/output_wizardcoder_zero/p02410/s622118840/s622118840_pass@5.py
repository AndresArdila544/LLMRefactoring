def dot_product(n, m):
    try:
        matrix = [int(input()) for _ in range(n)]
        vector = [int(input()) for _ in range(m)
    except ValueError:
        return "Input Error"
        
    for num in dot(matrix,vector):
        print(num)

dot_product(int(input()), int(input()))