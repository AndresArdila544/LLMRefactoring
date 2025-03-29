def sa(Type=int):
    return list(map(Type, input().split()))

def solve():
  while True:
    h, w = sa()
    if not (h and w):
        break
    print(''.join(['.']*w + ['#', '#']*(w+2)) * h)
    print('\n'.join('#'*(h+2))

if __name__ == '__main__':
  # sys.stdin = open('input.txt', 'r')
  solve()