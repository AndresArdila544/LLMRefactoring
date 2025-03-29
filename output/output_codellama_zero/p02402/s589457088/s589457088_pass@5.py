Here is a refactoring of your original code:
n = int(input())
x = list(map(int, input().split()))
print(f"{min(x)} {max(x)} {sum(x)}")