def main():
    while True:
        num = input()
        if num == '0 0':
            break
        x, y = map(int, num.split())
        if x > y:
            print(y, ' ', x)
        else:
            print(num)

main()