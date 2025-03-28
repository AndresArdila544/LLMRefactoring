```python
def main():
    while True:
        m, f, r = map(int, input().split())
        if m == -1 and f == -1 and r == -1:
            break
        elif m + f >= 80:
            print("A")
        elif m + f >= 65 or (m + f >= 30 and r >= 50):
            print("B")
        else:
            print("C") if r < 50 else print("D")
``` 

# The code is now more concise, with fewer lines of code and reduced complexity.