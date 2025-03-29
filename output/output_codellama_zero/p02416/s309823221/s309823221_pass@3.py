# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_B&lang=jp

"""
import sys
from sys import stdin
input = stdin.readline

def main(args):
    while True:
        x = int(input())
        if x == 0: break
        print(sum(map(int, str(x))))

if __name__ == '__main__':
    main(sys.argv[1:])