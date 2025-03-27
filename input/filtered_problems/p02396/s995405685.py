import sys
a = []
for l in sys.stdin:
    a.append(int(l))
    
for i in range(len(a)-1):
    print('Case '+str(i+1)+':' + ' '+str(a[i]))
