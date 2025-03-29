Here is a possible refactoring of the original code:

import statistics

while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(float, input().split()))
    average = statistics.mean(a)
    std_dev = statistics.stdev(a)