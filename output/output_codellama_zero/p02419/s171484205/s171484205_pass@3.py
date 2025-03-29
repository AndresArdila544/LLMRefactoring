from sys import stdin
w = input().lower()
print(sum(t.count(w) for t in stdin.read().split()))