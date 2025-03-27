Here is the refactored code:

import math
n =int(input())
X=list(map(int, input().split()))
Y=list(map(int, input().split()))
s1=sum([abs(x-y) for x, y in zip(X, Y)])
s2=math.sqrt(sum([(x-y)**2 for x, y in zip(X, Y)]))
s3=math.pow(sum([(x-y)**3 for x, y in zip(X, Y)]),1/3)
s4max=max([abs(x-y) for x, y in zip(X, Y)])
print('{:.6f}'.format(s1))
print('{:.6f}'.format(math.sqrt(s2)))
print('{:.6f}'.format(math.pow(s3,1/3)))
print('{:.6f}'.format(s4max))