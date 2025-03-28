def main():
    a = input()
    table = list(map(int, input().split()))
    print(min(table), max(table), sum(table))

main()