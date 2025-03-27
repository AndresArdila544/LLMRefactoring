result = []
while True:
     m, f, r = (int(x) for x in input().split())
    if m == -1 and f == -1 and r == -1:
        break
    grades = ["F", "A", "B", "C", "D"]
    result.append(grades[m + f >= 80] or grades[m + f >= 65] or grades[m + f >= 50] or grades[r >= 50] or "F")
for grade in result:
    print(grade)