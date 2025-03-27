def lessthen(a, b):
    return a < b
    
a,b,c = map(int,input().split())
print('Yes') if lessthen(a, b) and lessthen(b, c) else print('No')