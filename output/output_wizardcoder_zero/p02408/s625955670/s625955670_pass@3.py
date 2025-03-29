import sys

def to_str(symbol, num):
    return f'{symbol} {num}' if isinstance(num, int) else 'JOKER' # Using f-strings and type checking for readability

if __name__ == '__main__':
    symbols = ['S', 'H', 'C', 'D']
    cards = [to_str(symbols[i//13], i%13+1) if i<52 else to_str('JOKER') for i in range(52)] # Using list comprehension and modulo operator to generate 52 cards (S1-14, H1-14, D1-14, C1-14)
    n = int(input())
    if n == 52: sys.exit() 
    for i in range(n):
        cards.remove(input())
    print('\n'.join(cards))
    # Assuming the input is taken as a list of strings, we can directly remove them from the list.

The original code has been refactored to use list comprehension and f-strings for better readability and lesser lines. The if condition to check if n==52 has also been added within the same function.