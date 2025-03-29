```python
import math

def move(lon, lat, com):
    lon.insert(3 - (com == "E" or com == "W"), lon.pop(0 if com == "S" else 2))
    lat[0], lat[2] = lon[0], lon[2]


longitude, latitude = [1, 2, 6, 5], [1, 4, 6, 3]
commands = input().split()
for c in commands:
    move(longitude, latitude, c)
print("{}".format(longitude[0]))
```