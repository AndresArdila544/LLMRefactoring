import sys

def sa(Type=int):
    return [Type(x) for x in input().split()]

def solve(h, w):
    row = ['.'] * w
    row[0] = '#'
    row[-1] = '#'
    row = ''.join(row)
    frame = [row] * h
    frame[0] = '#' * w
    frame[-1] = '#' * w
    return '\n'.join(frame)

if __name__ == '__main__':
    while True:
        try:
            h, w = sa()
        except ValueError:
            break
        else:
            print(solve(h, w))