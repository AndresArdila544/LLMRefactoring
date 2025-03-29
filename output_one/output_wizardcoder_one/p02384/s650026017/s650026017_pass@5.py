def is_right_surface(a, b, c, d, e, f, top, front):
    def calc_sides(x, y):
        if [a, b, c, d, e, f].index(top) > [a, b, c, d, e, f].index(front):
            [tmp1, tmp2] = [front, top]
        else:
            [tmp1, tmp2] = [top, front]
        
        if [a, b, c, d, e, f].index(top) == 1 and [a, b, c, d, e, f].index(front) == 2:
            return c, d, [tmp1, tmp2][::-1]
        elif [a, b, c, d, e, f].index(top) == 1 and [a, b, c, d, e, f].index(front) == 3:
            return e, b, [tmp1, tmp2][::1]
        elif [a, b, c, d, e, f].index(top) == 1 and [a, b, c, d, e, f].index(front) == 4:
            return b, e, [tmp1, tmp2][::-1]
        elif [a, b, c, d, e, f].index(top) == 1 and [a, b, c, d, e, f].index(front) == 5:
            return d, c, [tmp1, tmp2][::1]
        elif [a, b, c, d, e, f].index(top) == 2 and [a, b, c, d, e, f].index(front) == 3:
            return a, f, [tmp1, tmp2][::-1]
        elif [a, b, c, d, e, f].index(top) == 2 and [a, b, c, d, e, f].index(front) == 4:
            return f, a, [tmp1, tmp2][::1]
        elif [a, b, c, d, e, f].index(top) == 2 and [a, b, c, d, e].index(front) == 6:
            return c, d, [tmp1, tmp2][::-1]
        elif [a, b, c, d, e, f].index(top) == 3 and [a, b, c, d, e].index(front) == 5:
            return a, f, [tmp1, tmp2][::1]
        elif [a, b, c, d, e, f].index(top) == 3 and [a, b, c, d, e].index(front) == 6:
            return e, b, [tmp1, tmp2][::-1]
        elif [a, b, c, d, e, f].index(top) == 4 and [a, b, c, d, e].index(front) == 5:
            return f, a, [tmp1, tmp2][::1]
        elif [a, b, c, d, e, f].index(top) == 4 and [a, b, c, d, e].index(front) == 6:
            return b, e, [tmp1, tmp2][::-1]
        else:
            return None, None, [tmp1, tmp2][::1]
    
    def move_sides(move_str):
        if "N" in move_str:
            a, b = b, e
            c, d = c, f
            e, f = a, d
        elif "E" in move_str:
            a, c = d, c
            d, f = a, f
        elif "W" in move_str:
            a, c = c, f
            d, f = a, d
        elif "S" in move_str:
            a, e = e, b
            b, e = a, e
            
    for _ in range(n):
        x, y = map(int, input().split())
        right, left, swap = calc_sides(x, y)
        if swap:
            print(left)
        else:
            print(right)