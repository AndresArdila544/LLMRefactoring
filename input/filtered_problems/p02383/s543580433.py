def move(lon, lat, com):
    target, other, pop_index, insert_index = lon, lat, 0, 3
    if com == "E" or com == "W":
        target, other = lat, lon
    if com == "S" or com == "W":
        pop_index, insert_index = 3, 0
    target.insert(insert_index, target.pop(pop_index))
    other[0], other[2] = target[0], target[2]


longitude = [1, 2, 6, 5]
latitude = [1, 4, 6, 3]
values = list(input().split())
command = input()
for c in command:
    move(longitude, latitude, c)
print("{}".format(values[longitude[0] - 1]))

