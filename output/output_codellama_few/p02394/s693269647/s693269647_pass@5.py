import sys
W,H,x,y,r = [int(i) for i in sys.stdin.readline().split()]
print('Yes' if x-r<=0 and 0<=y-r<=0 or x+r>=W and 0<=y+r<=H or 0<=x+r<=W and y-r<=0 and 0<=y+r<=H else 'No')