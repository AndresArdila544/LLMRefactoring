Below is the program that I have refactored in order to reduce its lines and complexity, while preserving its functionality:

while True:
    try:
        a = int(input())
        b = int(input())
    except:
        break
    print(min(a,b),max(a,b))