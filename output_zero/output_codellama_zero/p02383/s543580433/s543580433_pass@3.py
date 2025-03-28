Here is a refactored version of the original program:

def move(lon, lat, com):
    target, other, pop_index, insert_index = lon, lat, 0, 3
    if com in ["E", "W"]:
        target, other = lat, lon
    if com in ["S", "W"]:
        pop_index, insert_index = 3, 0
    target.insert(insert_index, target.pop(pop_index))
    other[0], other[2] = target[0], target[2]

longitude = [1, 2, 6, 5]
latitude = [1, 4, 6, 3]
command = input()
for c in command:
    move(longitude, latitude, c)
print("{}".format(values[lon[0] - 1]))