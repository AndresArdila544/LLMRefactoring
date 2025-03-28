def is_right_surface(a, b, c, d, e, f, top, front):
    if [top, front] == sorted([1, 2]) and (c, b, False) != (d, e, False):
        return a, d, True
    elif [top, front] == sorted([1, 3]):
        return c, b, True
    elif [top, front] == sorted([1, 4]:
        return b, e, True
    elif [top, front] == sorted([1, 5]):
        return d, c, False
    elif [top, front] == sorted([2, 3]):
        return a, f, True
    elif [top, front] == sorted([2, 4]:
        return f, a, True
    elif [top, front] == sorted([2, 6]):
        return c, d, False
    elif [top, front] == sorted([3, 5]):
        return a, f, True
    elif [top, front] == sorted([3, 6]:
        return e, b, False
    elif [top, front] == sorted([4, 5]):
        return f, a, False
    elif [top, front] == sorted([4, 6]:
        return b, e, True
    else:
        return d, c, False
        
def move(n_list, moves):
    for i in moves:
        if i == "N":
            n_list[0], n_list[1] = n_list[1], n_list[2]
            n_list[2], n_list[3] = n_list[5], n_list[4]
            n_list[4], n_list[5] = n_list[0], n_list[1]
        elif i == "E":
            n_list[0], n_list[2] = n_list[3], n_list[0]
            n_list[1], n_list[3] = n_list[4], n_list[1]
            n_list[2], n_list[4] = n_list[5], n_list[2]
        elif i == "W":
            n_list[0], n_list[3] = n_list[4], n_list[0]
            n_list[1], n_list[4] = n_list[5], n_list[1]
    return n_list
            
a, b, c, d, e, f = map(int, input().split())
n_list = [0, a, b, c, d, e, f]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    result = is_right_surface(a, b, c, d, e, f, x, y)
    print("swapped" if result[2] else result[:2])
    
# 1 line version (using list comprehension and unpacking)
def is_right_surface(*args):
    return [*((*args[:5], False) if sorted(args[:2]) == [1,2] and args[0:2][::-1] != args[3:5] else (args[1], args[4], True) if args[:2] == [1,3] or args[:2] == [1,4] or args[:2] == [1,5] else (args[0], args[4], False) if args[:2] == [2,3] or args[:2] == [2,4] or args[:2] == [2,6] else (args[0], args[1], True) if args[:2] == [3,5] or args[:2] == [3,6] else (args[1], args[3], False) if args[:2] == [4,5] or args[:2] == [4,6] else (args[0], args[3])][-1]

def move(n_list, moves):
    for i in moves:
        if i == "N":
            n_list[0], n_list[1], n_list[2], n_list[3], n_list[4], n_list[5] = n_list[1], n_list[2], n_list[4], n_list[5], n_list[0]
        elif i == "E":
            n_list[0], n_list[2], n_list[3], n_list[4], n_list[5] = n_list[3], n_list[0], n_list[4], n_list[1]
        elif i == "W":
            n_list[0], n_list[3], n_list[4], n_list[5] = n_list[4], n_list[0], n_list[1], n_list[2]
    return n_list
    
a, b, c, d, e, f = map(int, input().split())
n_list = [0, a, b, c, d, e, f]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    print("swapped" if is_right_surface(*move(n_list, input().split() + ["N"])[2:] else (*is_right_surface(a, b, c, d, e, f, x, y), "W")