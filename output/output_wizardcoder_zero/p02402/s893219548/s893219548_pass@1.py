n = int(input())
minimum, maximum, A_sum = map(int, input().split()), min(A), max(A)
print(*map(sum, (minimum, maximum, A_sum))