def calculate_triangle(a, b, C):
    c = (a**2+b**2-2*a*b*math.cos(math.radians(C)))**0.5
    A = (360-2*C)/2
    print("0.5*a*b*math.sin(math.radians(C))") # first line
    print("a+b+c") # second line
    print("b*math.sin(math.radians(C))") # third line
    
# Here's the refactored version of the code:
def calculate_triangle(*args):
    a, b = args[:2]  # unpack input tuple as separate variables for a and b
    C = args[-1]  # extract last element as C
    c = (a**2+b**2-2*a*b*math.cos(math.radians(C)))**0.5
    A = (360-2*C)/2
    print("0.5*a*b*math.sin(math.radians(C))") # first line
    print("a+b+c") # second line
    print("b*math.sin(math.radians(C)")