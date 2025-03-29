```python
points_t = points_h = 0
for _ in range(int(input())):
    card1, card2 = map(float, input().split())
    if card1 > card2:
        points_t += 3
    elif card1 < card2:
        points_h += 3
    else:
        points_t += 1
        points_h += 1
print(points_t, points_h)
``` 
```python
points = {"T":0,"H":0}
for _ in range(int(input())):
    card1,card2=map(float, input().split())
    if card1 > card2:
        points["T"] += 3
    elif card1 < card2:
        points["H"] += 3
    else:
        points["T"] += 1
        points["H"] += 1
print(points["T"],points["H"])
``` 
```python
import math
points = {"T":0,"H":0}
for _ in range(int(input())):
    x1,y1,x2,y2=map(float, input().split())
    points["T"] += 3 if x1>x2 else 1
    points["H"] += 3 if y1<y2 else 1
print(*points.values()) 
``` 
```python
import math
for _ in range(int(input())):
    x1,y1,x2,y2=map(float, input().split())
    print(math.hypot(abs(x1-x2), abs(y1-y2)))
```