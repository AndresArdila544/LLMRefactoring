#!/usr/bin/python

a,b = (int(i) for i in input().split())

print(str(int(a/b)) + " " + str(a%b) + " " + str(a/b))