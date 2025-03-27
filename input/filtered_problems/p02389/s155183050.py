def area(a,b):
    return a*b
    
def perimeter(a,b):
    return (a+b)*2
    
s = input()
a,b = s.split()
a = int(a)
b = int(b)

print(area(a,b), perimeter(a,b))
