n = int(input())
tp = hp = 0
for i in range(n):
    tw,hw = map(int, input().split())
    tp += max(tw, hw) * 2 - min(tw, hw) + 1
print(f"{tp} {hp}")