n = int(input())
print(" ".join(str(i) for i in range(1, n+1 if i%3==0 else i for temp in range(n, 0, -1) if temp % 10 == 3), end="") + "\n"