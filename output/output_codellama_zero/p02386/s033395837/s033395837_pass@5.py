import itertools

num = int(input())
dice = [0 for i in range(num)]
rdice = [0 for i in range(num)]
ndice_ = [0 for i in range(num)]
ndice = [0 for i in range(num)]
nrdice = [0 for i in range(num)]
dice_norm = [0 for i in range(num)]
varif = [0 for i in range(num)]
varif_child = [0 for i in range(6)]

def cross(a,b):
	return((a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]))

for n in range(num):
	dice_[n] = [int(i) for i in input().split()]
	
	dice[n] = {
		(0,0,1):dice_[n][0],
		(0,-1,0):dice_[n][1],
		(1,0,0):dice_[n][2],
		(-1,0,0):dice_[n][3],
		(0,1,0):dice_[n][4],
		(0,0,-1):dice_[n][5]
	}

for n in range(num):
	dice_keys = [i for i in dice[n].keys()]
	for count,min_ in enumerate(dice_keys):
		opposing = tuple([-i for i in min_])
		sides = list(set(dice_keys) - set([opposing,min_]))
		one = sides[0]
		two = cross(min_, one)
		three = cross(min_, two)
		four = cross(min_, three)
		varif_child[count] = min([1*dice[n][min_] + 10*dice[n][on] + 100*dice[n][tw] + 1000*dice[n][th] + 10000*dice[n][fo] + 100000*dice[n][opposing] for on,tw,th,fo in [[one,two,three,four],[four,one,two,three],[three,four,one,two],[two,three,four,one]]])
	varif[n] = min(varif_child)

if len(list(set(varif))) == num:
	print("Yes")
else:
	print('No')