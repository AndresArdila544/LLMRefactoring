def execute(*args):
    return sorted(list(args))

if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    print(*execute(*numbers)

This program will take in three integers separated by space as input and sort them using the `sorted()` function before printing them out. It is more concise and easier to read than the previous version due to its use of the `*args` parameter, which allows the function to take an arbitrary number of arguments.