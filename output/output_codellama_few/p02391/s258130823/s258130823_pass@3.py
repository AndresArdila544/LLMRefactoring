import sys

def compare(s):
    s=input().rstrip().split(' ')
    a=int(s[0])
    b=int(s[1])
    if a>b:
        print("a > b")
    elif a<b:
        print("a < b")
    else:
        print("a == b")

if __name__ == "__main__":
    compare(sys.stdin.readline())