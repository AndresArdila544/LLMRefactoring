Here is a refactored version of the original Python program that has fewer lines and improved readability:

def get_next_input():
    return int(input())

def print_case(count, value):
    print('Case {0}: {1}'.format(count, value))

while True:
    x = get_next_input()
    
    if x == 0:
        break
    
    print_case(count, x)
    count += 1