import sys

def sa(Type=int):
    return list(map(Type, input().split()))

def solve(h, w):
    row = ['#' * w]
    frame = ['#' * w + '.'.join(row) + '#' * w] * h
    print(*frame, sep='\n', end='\n')

if __name__ == '__main__':
    while True:
        h, w = sa()

        if h == 0 and w == 0:
            break
        
        solve(h, w)