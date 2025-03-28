import sys


def f(H, W):
    so = ""
    se = ""

    for i in range(W):
        if i & 1:
            se += "."
            so += "#"
        else:
            se += "#"
            so += "."
    for i in range(H):
        print so if i & 1 else se


def main():
    sys.stdin = open('data.txt')

    while True:
        nums = map(int, raw_input().split())

        H = nums[0]
        W = nums[1]
        if H == 0 and W == 0:
            break

        f(H, W)


if __name__ == "__main__":
    main()