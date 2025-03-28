#!/usr/bin/env python
# coding: utf-8
import math

def main():
	r = float(raw_input())
	print round(math.pi * math.pow(r, 2), 6), round(math.pi * 2 * r, 6)

if __name__ == '__main__':
	main()