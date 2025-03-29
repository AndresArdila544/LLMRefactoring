n = int(input())
while True:
    alp = input()
    if alp == '-':
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        alp_list = list(alp)
        alp_list.insert(0, alp_list.pop(-h))
        print(''.join(alp_list))