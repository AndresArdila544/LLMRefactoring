while True:
    alp = input()
    if alp == '-':
        break

    m = int(input())
    for i in range(m):
        h = int(input())
        alp = alp[h:len(alp)] + alp[:h]
    print(alp)