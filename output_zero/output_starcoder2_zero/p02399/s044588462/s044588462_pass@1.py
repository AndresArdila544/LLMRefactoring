'''


def main():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    a = int(input())
    b = int(input())

    d = int(a / b)
    r = a % b
    f = float(a / b)

    print(str(d) + ' ' + str(r) + ' ' + str(f))


if __name__ == "__main__":
    main()