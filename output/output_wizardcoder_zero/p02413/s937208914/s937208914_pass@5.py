a = []
gyou = [0] * len(input().split())
retu = []
s = 0
c, r = map(int, input().split())

for _ in range(r): # instead of using 'range' for each loop, we can use a single loop
    a.append([*map(int, input().split())]) # instead of using multiple loops for appending elements to lists, we can unpack the map object directly into list creation
    retu.append(sum(a[-1]))
for i in range(len(gyou)):
    gyou[i] += a[i][i] # using indexing to access row and column
s = sum(gyou)
print(*[" ".join(map(str, a[i]) + str(retu[i]) for i in range(len(a))]) # use list comprehension instead of multiple print statements
      * [*map(str, gyou)] + [s]) # use unpacking to join lists and append the sum value