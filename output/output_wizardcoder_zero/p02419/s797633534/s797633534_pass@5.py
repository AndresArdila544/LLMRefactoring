for _ in range(int(input())):
    word = input().lower()
    count = sum([1 for i in map(str.split, [input(),] * 9) if word in i])
print(count-1)