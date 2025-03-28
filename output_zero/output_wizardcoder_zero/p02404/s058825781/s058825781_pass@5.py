XS = list(map(int, open(0).read().split()))
for H, W in zip(*[iter(XS)]*2):
    if not all((H,W): break
    print("{0}#{1}#{2}\n{3}{4}".format("#"*(W-2), "#"*2, "#"*(W-2), ("#{}#\n"*(H-2)).format(".")).rstrip())+"#"*(W)