def main():
    while True:
        m, f, r = map(int, input().split())
        if (m, f) == (-1,-1):
            break
        elif m < 0 or f < 0:
            print("F")
        else:
            total_marks = m + f
            if total_marks >= 80:
                print("A")
            elif total_marks >= 65 and r >= 50:
                print("B")
            elif total_marks >= 50:
                print("C")
            elif total_marks >= 30 and r < 50:
                print("D")
            else:
                print("F")

if __name__ == "__main__":
    main()