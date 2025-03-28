class Rect():
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self):
        for i in range(self.w):
            for j in range(self.h):
                sys.stdout.write("#" if (i+j) % 2 == 0 else ".")
            print("") # Use string concatenation and f-string instead of `sys.stdout.write` to make code cleaner
        print("\n")

def main():
    data = []
    while True:
        n = input().split()
        w, h = int(n[0]), int(n[1])
        if not all(i.isdigit() for i in n): # Check if input is valid using list comprehension and `all` function to break the loop when 0 values are entered.
            break
        data.append(Rect(int(w), int(h))
    
    for num in data:
        num.draw()

if __name__ == "__main__":
    main()