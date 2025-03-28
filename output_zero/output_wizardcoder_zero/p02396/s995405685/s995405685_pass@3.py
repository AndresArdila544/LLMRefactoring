a = list(map(int, sys.stdin))
print(*['Case '+str(i)+': ' + str(x) for i, x in enumerate(a, 1)])