#Refactored code
radius = int(input())
width = int(input())
height = int(input())
x_coord = int(input())
y_coord = int(input())

if radius <= x_coord and x_coord <= width and y_coord <= height:
    print("Yes")
else:
    print("No")