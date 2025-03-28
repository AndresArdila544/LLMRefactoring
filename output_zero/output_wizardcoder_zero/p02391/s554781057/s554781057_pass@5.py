a, b = map(int, input().split())
print("{0} {1} {2}".format('a', 'b' if a < b else ('<' if a > b else '==') , 'b'))