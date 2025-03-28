def func(x, y):
    tmp = [[0 for i in range(6)] for j in range(n+1)]
    max = 0
    for i in range(1, n+1, 1):
        absDiff = abs(x[i]-y[i])
        tmp[i][0] = absDiff
        tmp[i][1] = absDiff ** 2
        tmp[i][2] = tmp[i][1] * absDiff
        tmp[i][3] = tmp[i-1][3] + tmp[i][0]
        tmp[i][4] = tmp[i-1][4] + tmp[i][1]
        tmp[i][5] = tmp[i-1][5] + tmp[i][2]
        if absDiff > max:
            max = absDiff
    return [tmp[n][3], math.sqrt(tmp[n][4]), math.cbrt(tmp[n][5]), max]