if __name__ == '__main__':
    matrix_size = [int(x) for x in input().split(' ')]
    matrix = [[int(y) for y in input().split(' ')] for i in range(matrix_size[0])]
    vector_b = [int(input()) for i in range(matrix_size[1])]
    result = [sum([x*y for x, y in zip(row, vec)]) for row in matrix for vec in vector_b]
    print(*result)