```python
import sys
class Rect():
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def draw(self):
        for i in range(self.w):
            for j in range(self.h):
                sys.stdout.write("#" if (i+j) % 2 == 0 else ".")
            sys.stdout.write("\n")
            
def main():
    while True:
        w, h = map(int, input().split())
        if w == h == 0:
            break
        Rect(w,h).draw()

if __name__ == "__main__":
    main()
```