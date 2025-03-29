Here is what we mean by "more concise": our goal is to make it so that all of the statements in the program are on a single line. 
For example:

    for row in range(n):
        for col in range(l):
            sum_v = 0
            for k in range(m):
                sum_v += A[row][k] * B[k][col]
            C[row][col] = sum_v


would be condensed to:

    C[row][col] = sum([A[row][k]*B[k][col] for k in range(m)])

Please also write an informal, plain English explanation about the reasons that you choose each form of expression over others (you don't have to actually provide any Python code).