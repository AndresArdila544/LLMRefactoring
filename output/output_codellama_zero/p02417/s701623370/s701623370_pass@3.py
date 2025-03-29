import sys
print(*[f"{chr(i): {s.count(chr(i))}" for i in range(97,123)], sep="\n")