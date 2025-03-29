import sys

def to_str(symbol, num):
    return '{0} {1}'.format(symbol, num)

if __name__ == '__main__':
    symbols = ['S','H','C','D']
    cards = [to_str(x,y) for x in symbols for y in range(1,14)]
    n = int(input())
    if n == 52: sys.exit()
    input_cards = [input() for i in range(n)]
    print('\n'.join(set(cards).difference(input_cards)))