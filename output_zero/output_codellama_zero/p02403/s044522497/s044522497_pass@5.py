def main():
    while True:
        a, b = map(int, input().split())
        if a == 0: break
        print('#'*b)

if __name__ == '__main__':
    main()