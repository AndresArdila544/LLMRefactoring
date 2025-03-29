This is an example of refactoring; reducing its lines and complexity, while preserving its functionality.
Example:

import math

x1, y1, x2, y2 = map(float, input().split())

dx  = x1 - x2
dy  = y1 - y2

d  = math.hypot(dx, dy)

print(d)

Refactored version:

import math
x1, y1, x2, y2  = map(float, input().split())
d  = math.hypot(x1-x2, y1-y2)
print(d)

Example 2:

n  = int(input())
for i in range(1, n+1):
    if i % 3 == 0:
        print('', i, end = '')
    elif '3' in str(i):
        print('', i, end = '')
print()

Refactored version:

n  = int(input())
for i in range(1, n+1):
    if i % 3 == 0 or '3' in str(i):
        print('', i, end='')

Example 3:

n,m,l  = map(int,input().split())
YEAH  = [list(map(int,input().split())) for i in range(n)]
FUCK  = [list(map(int,input().split())) for i in range(m)]

for i in range(n):
    for j in range(l):
        GOMI  = 0
        for k in range(m):
            GOMI  += FUCK[k][j]*YEAH[i][k]
        if j!=l:
            print(GOMI)
        else:
            print(GOMI,end="  ")
    print()

Refactored version:

n,m,l  = map(int,input().split())
YEAH  = [list(map(int,input().split())) for i in range(n)]
FUCK  = [list(map(int,input().split())) for i in range(m)]

for i in range(n):
    GOMI_list  = []
    for j in range(l):
        GOMI  = 0
        for k in range(m):
            GOMI  += FUCK[k][j]*YEAH[i][k]
        GOMI_list.append(GOMI)
    print(*GOMI_list,sep='  ')

Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:

judge = True

while judge:
    N  = list(map(int,input().split()))
    if N[0] + N[1] == 0:
        judge = False #finish
    else:
        for i in range(0, N[0]):# H
            print("#",end="")
            if i == 0 or i == (N[0] - 1):
                for j in range(1, N[1]-1):
                    print("#",end="")
                print("#")
            else:
                for j in range(1, N[1]-1):
                    print(".",end="")
                print("#")

    print("\n",end="")



Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code, no quotations. Just the code.