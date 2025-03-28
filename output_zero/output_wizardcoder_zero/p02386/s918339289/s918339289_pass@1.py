def flip_dice(n):
    dice = [[int(x) for x in input().split()] for i in range(n)]
    def flip_direction(d1, d2, face_set):
        if len(face_set) < 4:
            return random.choice([d1.east(), d1.south(), d1.north()])
        elif not (d1[0] == d2[0] and d1[1] == d2[1]):
            return d1.east()
        else:
            return random.choice([d1.north(), d1.south()]) if d1[3] != d2[3] else d1.north()
    
    for i in range(len(dice)):
        faces = set(range(4)) - {i % 4}
        for j in range(len(dice)):
            if i >= j or len(set(dice[i]) ^ set(dice[j])) != faces:
                continue
            flip_direction(dice[i], dice[j], faces)
    
    for i in range(len(dice)):
        if all(d1 == d2 for d1, d2 in zip(dice[i][:4], dice[(i+1) % n]) and dice[i][0] == dice[(i-1)%n][0]:
            return "No"
    
    return "Yes"