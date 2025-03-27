def execute(a, b, c):
     return sorted([a,b,c])
 if __name__ == '__main__':
     numbers = [int(x) for x in input().split(' ')]
     print(*execute(*numbers))