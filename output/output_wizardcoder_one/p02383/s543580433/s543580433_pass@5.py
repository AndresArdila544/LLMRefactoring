```python
import math

lon = [1,2,6,5]
lat = [1,4,6,3]
values = list(map(float, input().split()))
com = input()
for c in com:
    if c == "E" or c == "W":
        lon.append(lon.pop(2))
    elif c == "S" or c == "N":
        lat.insert(3,lat.pop(0))
print("{:.2f}".format(math.hypot(abs(values[1]-values[5], abs(values[2]-values[4]) if com in ["E","W"] else abs(values[3]-values[4]))))