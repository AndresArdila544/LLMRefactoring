def move(lon, lat, com):
    target, other, pop_index = [latitude, longitude][com in ['E', 'W'], latitude, longitude][com in ['S', 'N']], 3
    other[0], other[2] = target.pop(pop_index), target[0] if com == 'E' or com == 'W' else target[2]
print('{}'.format([longitude, latitude][com in ['S', 'N']])