r = float(input())
print('{:.6f} {:.6f}'.format(math.pi*r**2, 2*math.pi*r)) # Note that this assumes you want to calculate the area and perimeter of a circle with radius r in one line. If you want to separate them into different lines, you can do so as follows:
area = math.pi * r ** 2
perimeter = 2 * math.pi * r
print('{:.6f} {:.6f}'.format(area, perimeter))