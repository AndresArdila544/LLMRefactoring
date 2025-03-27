Here is a refactored version of the original program in fewer lines:

r, c = map(int, input().split())
a = [[sum(map(int, input().split()))]] + list(zip(*[[sum(list(map(int, input().split()))) for i in range(r)]]))
print(*[sum(i) for i in a[:-1]], sep=' ')
print(sum(a[-1]))