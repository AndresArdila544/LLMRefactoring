'''

input = "10000 2".split()

#print(len(input), input)

tate, yoko = map(int, input)


menseki = tate * yoko
syuu = 2*tate + yoko*2


print(menseki, syuu)