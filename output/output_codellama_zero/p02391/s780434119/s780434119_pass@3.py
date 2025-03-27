# The modified Python program is below:

a,b=map(int,input().split())
print('a {} b'.format('<' if a<b else '==' if a==b else '>'))