import sys

def main():
    while True:
        line = sys.stdin.readline()
        if line == '0 0\n':
            break
        elif len(line) != 10:
            print('error')
            exit()
        H, W = map(int, line.split())
        for i in range(H):
            print('#' * (W-2))
        print('\n')
if __name__ == "__main__":
    main()