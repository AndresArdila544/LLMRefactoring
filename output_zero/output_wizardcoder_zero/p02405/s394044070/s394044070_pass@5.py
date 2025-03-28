```python
import sys

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self):
        for i in range(self.width):
            row = ""
            for j in range(self.height):
                if (i+j) % 2 == 0:
                    row += "#"
                else:
                    row += "."
            print(row)
            
def main():
    while True:
        dimensions = input().split()
        width, height = int(dimensions[0]), int(dimensions[1])
        if not all(dimensions):
            break
        Rectangle(width, height).draw()

if __name__ == "__main__":
    main()
```