import sys
input = lambda: sys.stdin.readline()
def main():
    while True:
        x=int(input())
        if x==0:break
        digit_sum=0
        while x:
            digit_sum+=x%10
            x//=10
        print(digit_sum)
if __name__ == '__main__':
    main()