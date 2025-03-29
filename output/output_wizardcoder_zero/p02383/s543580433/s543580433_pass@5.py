def move(lon_lat, com):
    target = lon_lat[2] if com == "N" else lon_lat[0]
    other = [1, 2, 6, 5] if com in {"E", "S"} else [1, 4, 6, 3]
    lon_lat.insert(int(com in {"W", "S"}), target)
    other[0], lon_lat[-1] = lon_lat[2], target

lon, lat = list(map(list, zip(*input().split()))[:-1])
move(lon, "E")
print("{}".format(lon[1]))