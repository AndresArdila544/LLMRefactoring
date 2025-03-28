Here is the refactored code:

def move(lon, lat, com):
    other = lon if com in ("E", "W") else lat
    pop_index = 2 if com == "S" else 3
    insert_index = 0 if com == "S" else 3
    target.insert(insert_index, target.pop(pop_index))
    other[0], other[2] = target[0], target[2]

longitude = [1, 2, 6, 5]
latitude = [1, 4, 6, 3]
values = list(input().split())
command = input()
for c in command:
    move(longitude, latitude, c)
print("{}".format(values[longitude[0] - 1]))