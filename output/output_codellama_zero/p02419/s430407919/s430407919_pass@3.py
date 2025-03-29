Here is a refactored version of the program with fewer lines and improved readability:

T = input()
W = input()
count = 0
while T != 'END_OF_TEXT':
    count += T.lower().split().count(W.lower())
    T = input()
print(count)