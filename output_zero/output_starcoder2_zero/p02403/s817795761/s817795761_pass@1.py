Below is my refactored version:
#  -*- coding: utf-8  -*
while True:
    h, w = map(int, input().split())

    if h == 0 and w == 0:
        break
    print('\n'.join(['#' * w] * h))