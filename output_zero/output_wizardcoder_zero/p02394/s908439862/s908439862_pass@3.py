```python
radius = float(input())
width, height = map(float, input().split())
center_x, center_y = map(float, input().split())
if (0 <= center_x <= width - radius) and (0 <= center_y <= height - radius):
    print("Yes")
else:
    print("No")