def sum_digits(string):
    return sum(map(int, string))

while True:
    s = input()
    if s != '0':
        print(sum_digits(s))
    else:
        break