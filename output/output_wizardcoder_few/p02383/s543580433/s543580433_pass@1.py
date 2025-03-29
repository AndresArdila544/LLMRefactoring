```python
def move(lon, lat, com):
    target, other = lon if (com in ["E", "W"] else lat, lat if (com in ["N", "S"]) else lon
    target.insert(2, target.pop(0 if com == "W" or com == "S" else 1)
    other[0], other[1] = target[0], target[1]

lon = [1, 2, 6, 5]
lat = [1, 4, 6, 3]
command = input()
for c in command:
    move(lon, lat, c)
print("{}".format(lon[0]))
```