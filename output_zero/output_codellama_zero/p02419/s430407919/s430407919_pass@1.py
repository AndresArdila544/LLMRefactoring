W = input()
T = input()
while T != 'END_OF_TEXT':
    count += T.lower().count(W.lower())
    T = input()
print(count)