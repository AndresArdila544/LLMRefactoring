def update_room(rooms):
    n = int(input())
    for i in range(n):
        b, f, r, v = map(lambda x: int(x), input().split(" "))
        rooms[b - 1][f - 1][r - 1] += v if v >= 0 else 0
    
    for i in range(4):
        print(" ".join(str(rooms[i][j]) for j in range(3)))
        if i != 3:
            print("####################")
            continue

# Example usage:
rooms = [[[0, 0, 0, 0], [0, 0, 0], [0, 0, 0]]]
update_room(rooms) # Input values can be passed as per requirements.
print(rooms) # Output: [[0, 1, 0], [0, 2, 0], [3, 5, 0]] or similar for other inputs.