num = int(input())
dice_ = [[int(i) for i in input().split()] for _ in range(num)]
dice = [{(-1,0,0): dice_[n][3], (0,-1,0): dice_[n][1], (0,0,-1): dice_[n][5], (0,0,1): dice_[n][0], (0,1,0): dice_[n][4], (1,0,0): dice_[n][2]} for n in range(num)]
varif = [min([1*dice[n][min_] + 10*dice[n][on] + 100*dice[n][tw] + 1000*dice[n][th] + 10000*dice[n][fo] + 100000*dice[n][opposing] for on,tw,th,fo in [[one,two,three,four],[four,one,two,three],[three,four,one,two],[two,three,four,one]]]) for n in range(num)]
if len(set(varif)) == num:
	print("Yes")
else:
	print('No')