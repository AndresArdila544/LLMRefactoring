```python
def move(lon, lat, com):
    target, other = lon if com in ["E", "W"] else lat, lat if com in ["N", "S"] else lon
    for i, j in enumerate([3, 0]):
        if com in {"E", "W"}:
            lon.insert(j, lon.pop(i))
        elif com in {"N", "S"}:
            lat.insert(j, lat.pop(i))
    other[0], other[2] = target[0], target[2]

lon = [1, 2, 6, 5]
lat = [1, 4, 6, 3]
com = input()
for c in com:
    move(lon, lat, c)
print("{}".format(lon[0]))
```