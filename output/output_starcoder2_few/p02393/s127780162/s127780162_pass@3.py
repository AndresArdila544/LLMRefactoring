This is an example of refactoring; reducing its lines and complexity, while preserving its functionality.
Example:

import math
x1, y1, x2, y2  = map(float, input().split())
dx = x1 - x2
dy = y1 - y2
d = math.hypot(dx, dy)
print(d)
Refactored version: import mathx1,y1,x2,y2=map(float,input().split())d=math.hypot(x1-x2,y1-y2)print(d)Example 2: n = int(input())for i in range(1,n+1):if i % 3 == 0:print('',i, end = '')elif '3' in str(i):print('', i, end = '')print()
Refactored version:n = int(input())for i in range(1,n+1):if i % 3 == 0 or '3' in str(i):print('', i, end='')Example 3: n,m,l = map(int,input().split())YEAH = [list(map(int,input().split())) for i in range(n)]FUCK = [list(map(int,input().split())) for i in range(m)]for i in range(n):GOMI_list = []for j in range(l):GOMI = 0for k in range(m):GOMI += FUCK[k][j]*YEAH[i][k]GOMI_list.append(GOMI)print(*GOMI_list,sep=' ')Refactored version:n,m,l = map(int,input().split())YEAH = [list(map(int,input().split())) for i in range(n)]FUCK = [list(map(int,input().split())) for i in range(m)]for i in range(n):GOMI_list = []for j in range(l):GOMI = 0for k in range(m):GOMI += FUCK[k][j]*YEAH[i][k]GOMI_list.append(GOMI)print(*GOMI_list,sep=' ')Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability. Here is the original Python program:x = raw_input().split()m = map(int,x)m.sort()a = m[0]b = m[1]c = m[2]print a,b,cPlease provide the refactored version of the code with fewer lines and improved readability. DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code, no quotations. Just the code.