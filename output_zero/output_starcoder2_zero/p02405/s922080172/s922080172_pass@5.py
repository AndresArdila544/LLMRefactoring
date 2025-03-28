Refactored Code: 

from sys import stdin as f
XS = list(map(int, f.read().split()))
B  = ["#."*150, ".#"*150]
for i in range(0, len(XS), 2):
    H = XS[i]
    W = XS[i+1]
    if H == 0 and W == 0:
        break

    # I'm not sure about the indentation here. The next block of code would be indented one more level than the for loop, so it's a little weird to me. 
    # Is this correct? 

    for j in range(H):
        print(B[j%2][0:W])
    print("")




I tried to use your test cases as well to make sure my refactored code worked properly. It did!