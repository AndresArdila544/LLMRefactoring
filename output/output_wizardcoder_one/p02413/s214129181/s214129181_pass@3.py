a, b = map(int, input().split())
bs = [list(map(int, input().split())) for i in range(a)]
bs.append([sum(row) for row in zip(*bs)]);  # Refactored version of bs[i].append(sum(bs[i])
for row in bs:
    print(" ".join(map(str, row))