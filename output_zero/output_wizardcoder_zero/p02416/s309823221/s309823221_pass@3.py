import sys
from sys import stdin
input = stdin.readline

def main():
    while True:
        x = int(input())
        if not x: break
        
        digit_sum = sum(int(i) for i in str(x))
        print(digit_sum)

if __name__ == '__main__':
    main()