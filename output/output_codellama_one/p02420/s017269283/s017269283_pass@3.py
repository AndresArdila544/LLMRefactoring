while True:
    alp = input()
    if alp == '-':
        break
    for _ in range(int(input())):
        h = int(input())
        alp = alp[h:len(alp)] + alp[:h]