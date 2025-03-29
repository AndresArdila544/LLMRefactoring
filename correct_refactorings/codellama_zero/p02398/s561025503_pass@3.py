x = input().split()
print(len([i for i in range(int(x[0]), int(x[1]) + 1) if int(x[2]) % i == 0]))