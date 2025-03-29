import math
dim=int(input().strip())
vec_x=[int(i) for i in input().split()]
vec_y=[int(i) for i in input().split()]
abs_xy=[abs(vec_x[i]-vec_y[i]) for i in range(dim)]
dist_1=sum(abs_xy)
dist_2=math.sqrt(sum([i**2 for i in abs_xy]))
dist_3=max(abs_xy)
print("{:.5f}\n{:.5f}\n{:.5f}\n{:.5f}".format(dist_1,dist_2,dist_3))