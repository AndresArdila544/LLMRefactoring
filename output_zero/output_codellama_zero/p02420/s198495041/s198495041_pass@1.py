while True:
    C = input()
    if C == '-':
        break
    for _ in range(int(input())):
        C += input()[:int(input())]