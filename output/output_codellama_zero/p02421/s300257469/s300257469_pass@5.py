n = int(raw_input())
tp=0;hp=0
for i in range(n):
    tw,hw=raw_input().split()
    tp+=(tw==hw)
    hp+=(tw>hw)*3+(tw<hw)*3
print '%s %s' % (tp,hp)