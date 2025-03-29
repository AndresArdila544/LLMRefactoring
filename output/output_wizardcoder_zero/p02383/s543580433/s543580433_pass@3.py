def move(lon, lat, com):
    target, other, pop_index = lon, lat, 3 if "E" in com else lon if "W" in com else lat
    insert_index = (0 if "S" in com or "N" not in com else 2) if "W" in com else (2 if "E" in com or "N" not in com else 3)
    target.insert(insert_index, target.pop(pop_index))
    other[0], other[2] = (target[0], target[2]) if "S" in com else (other[1], other[3])

lon, lat = [1, 2, 6, 5], [1, 4, 6, 3]
for c in input().split():
    move(lon, lat, c)
print(lon)
print("{}".format(lon[0]))

# The refactored code uses list comprehension and ternary operators to make the code more concise. The function now takes only two arguments instead of three.