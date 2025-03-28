Here is a refactored version of the code:

#!/usr/bin/env python
# coding: utf-8
import math

def main():
	r = float(input())
	print("{0:.6f} {1:.6f}".format(math.pi * r ** 2, math.pi * 2 * r))

if __name__ == '__main__':
	main()