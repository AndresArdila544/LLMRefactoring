def move(lon, lat, com):
    target, other = lon, lat
    if com == "E" or com == "W":
        target, other = lat, lon
    if com in ["S", "W"]:
        target.pop(3)
        other[0], other[2] = target[0], target[2]

longitude = [1, 2, 6, 5]
latitude = [1, 4, 6, 3]
values = list(map(float, input().split()))
for c in input():
    move([longitude, latitude], c)
print("{}".format(values[0]))