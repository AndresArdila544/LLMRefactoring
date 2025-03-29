Here is a refactored version of the code:

def execute(a, b, c):
    return sorted([a, b, c])

if __name__ == '__main__':
    numbers = [int(i) for i in input().split(' ')]
    print(*execute(*numbers))