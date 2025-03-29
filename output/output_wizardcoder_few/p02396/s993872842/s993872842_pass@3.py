counter = 1
while True:
    x = input()
    if x == '0':
        break
    print("Case {}: {}".format(counter, x)
        
        counter += 1

Refactored version (with fewer lines and improved readability):

for i in itertools.count(start=1):
    x = input()
    if x == '0':
        break
    print("Case {}: {}".format(i, x)
        
Refactored version with even fewer lines:

print(*["Case {}:\n{}\n".format(i,x) for i in itertools.count(1) if input()!='0'])