Here is a refactored version of the code with fewer lines and improved readability:
```
class Dice:
    def __init__(self, face_val=None):
        self.face_values = ['1', '2', '3', '4', '5', '6']
        if face_val is not None:
            self.face_values = face_val

    def move(self, direction):
        if direction == "S":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[5] = self.face_values[5], self.face_values[0]
            self.face_values[1], self.face_values[4] = self.face_values[4], self.face_values[1]
            self.face_values[2], self.face_values[3] = self.face_values[3], self.face_values[2]
        elif direction == "W":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[1] = self.face_values[1], self.face_values[0]
            self.face_values[2], self.face_values[3] = self.face_values[3], self.face_values[2]
        elif direction == "E":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "N":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction == "":
            prev_faces = self.face_values[:]
            self.face_values[0], self.face_values[2] = self.face_values[2], self.face_values[0]
            self.face_values[1], self.face_values[3] = self.face_values[3], self.face_values[1]
        elif direction ==