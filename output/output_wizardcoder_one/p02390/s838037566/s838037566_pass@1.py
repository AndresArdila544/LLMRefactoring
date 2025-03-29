S = int(input())
h = S // (60*60)
m = (S - h * 36000) // 60
s = S % 60
print("{}:{}:{}".format(h, m, s))