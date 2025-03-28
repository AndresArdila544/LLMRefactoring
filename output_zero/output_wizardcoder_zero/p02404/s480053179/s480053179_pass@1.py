import sys

def sa(Type=int):
    return list(map(Type, input().split()))


def solve():
  h, w = sa()
  row = ['#' + '.'.join(['.' * (w - 2)] + '#') if i == 0 or i == h-1 else '.' * w for i in range(h) ]
  print('\n'.join(row))

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        while True:
            try:
                solve(*sa())
            except EOFError:
                break