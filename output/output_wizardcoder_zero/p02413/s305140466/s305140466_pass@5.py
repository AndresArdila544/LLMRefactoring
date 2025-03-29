def main():
    c, r = map(int, input().split())
    last_list = [0] * r
    for _ in range(c):
        x = input()
        sum_list = list(map(int, x.split()))
        for i in range(r):
            last_list[i] += sum_list[i]
        print("{} {}".format(x, sum(sum_list)))
    total_sum = 0
    for a in last_list:
        total_sum += a
    print(*last_list, total_sum)

if __name__ == "__main__": main()