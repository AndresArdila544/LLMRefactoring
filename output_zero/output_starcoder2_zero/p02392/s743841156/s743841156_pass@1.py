Here is my solution (less complex than the original):

def lessthen(a, b):
    return a < b
    
def range(a, b, c):
    return lessthen(a,b) and lessthen(b,c)

a,b,c = map(int, input().split())
if (range(a,b,c)):
    print('Yes')
else:
    print('No')