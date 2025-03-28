import sys as s
s = s.stdin.read().lower()
a = [print(i,":",s.count(i)) for i in map(chr,range(97,123))]