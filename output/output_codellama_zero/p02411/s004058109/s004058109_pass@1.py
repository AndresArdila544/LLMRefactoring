The following is a refactored version of the original Python program with fewer lines and improved readability:

while True:
    m, f, r = map(int, input().split())
    if m == -1 or f == -1:
        break
    
    s = m + f
    
    if s < 30:
        print('F')
    elif s < 50 and r < 50:
        print('D')
    elif s < 65:
        print('C')
    elif s < 80:
        print('B')
    else:
        print('A')