W = input().lower()
T = input().lower()
while T != 'END_OF_TEXT':
    count += T.count(W)
    T = input().lower()