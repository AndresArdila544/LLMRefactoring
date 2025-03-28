def to_str(symbol, num):
    return f'{symbol} {num}'

if __name__ == '__main__':
    symbols = ['S', 'H', 'C', 'D']
    cards = [to_str(x, y) for x in symbols for y in range(1, 14)]
    n = int(input())
    if n != 52:
        [cards.remove(input()) for _ in range(n)]
    print('\n'.join(cards))