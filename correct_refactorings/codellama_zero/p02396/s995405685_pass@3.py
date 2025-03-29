import sys
a = [int(l) for l in sys.stdin]
for i in range(len(a)-1):
    print('Case '+str(i+1)+':' +' '+str(a[i]))