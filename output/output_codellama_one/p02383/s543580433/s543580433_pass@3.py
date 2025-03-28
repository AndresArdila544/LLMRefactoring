import math

def move(lon, lat, com):
    target = lon if com == "E" or com == "W" else lat
    other = lon if com == "S" or com == "W" else lat
    pop_index = 0 if com == "S" or com == "W" else 3
    insert_index = 0 if com == "S" or com == "W" else 3
    target.insert(insert_index, target.pop(pop_index))
    other[0], other[2] = target[0], target[2]


longitude = [1, 2, 6, 5]
latitude = [1, 4, 6, 3]
values = list(input().split())
command = input()
for c in command:
    move(longitude, latitude, c)
print("{}".format(values[longitude[0] - 1]))