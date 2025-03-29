import math
while True:
    try:
        n = int(input())
        if not n:
            break
        
        data = list(map(int, input().split()))
        m = sum(data) / n
        mean_squared_error = sum((x - m) ** 2 for x in data) / n
        result = math.sqrt(mean_squared_error)
        
        print(result)
    except ValueError:
        continue