def main():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0: break
        print((a,b) if a >= b else (b,a))

if __name__ == "__main__":
    main()