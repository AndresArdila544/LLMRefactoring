import sys
print(" ".join(sorted([int(x) for x in sys.stdin.readline().split()]) + ["Sum of", "Minimum", "Maximum"]))