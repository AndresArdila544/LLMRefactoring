n = input()
n = int(n)
an = input()
an = an.split()
out_c1 = ''
for a in reversed(an):
    out_c1 = '{} {}'.format(out_c1,a)
else:
    out_c1 = out_c1[1:]
    print(out_c1)

