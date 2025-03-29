def execute(a, b, c):
    return sorted([a, b, c])

if __name__ == '__main__':
    numbers = map(int, input().split(' '))
    print(*sorted(numbers))