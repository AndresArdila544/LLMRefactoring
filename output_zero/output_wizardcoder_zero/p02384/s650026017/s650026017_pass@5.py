def Dice(a, b, c, d, e, f):
    def is_right_surface(top, front):
        swapped = False
        if n_list.index(top) > n_list.index(front):
            top, front = front, top
            swapped = True
        if (n_list.index(top), n_list.index(front)) == (1, 2):
            return c, d, swapped
        elif (n_list.index(top), n_list.index(front)) == (1, 3):
            return e, b, swapped
        elif (n_list.index(top), n_list.index(front)) == (1, 4):
            return b, e, swapped
        elif (n_list.index(top), n_list.index(front)) == (1, 5):
            return d, c, swapped
        elif (n_list.index(top), n_list.index(front)) == (2, 3):
            return a, f, swapped
        elif (n_list.index(top), n_list.index(front)) == (2, 4):
            return f, a, swapped
        elif (n_list.index(top), n_list.index(front)) == (2, 6):
            return c, d, swapped
        elif (n_list.index(top), n_list.index(front)) == (3, 5):
            return a, f, swapped
        elif (n_list.index(top), n_list.index(front)) == (3, 6):
            return e, b, swapped
        elif (n_list.index(top), n_list.index(front)) == (4, 5):
            return f, a, swapped
        elif (n_list.index(top), n_list.index(front)) == (4, 6):
            return b, e, swapped
        elif (n_list.index(top), n_list.index(front)) == (5, 6):
            return d, c, swapped
    n_list = [0, a, b, c, d, e, f]
    
    def move(move_str):
        for i in move_str:
            if i == "N":
                tmp1, tmp2 = b, f
                a, b, e = a, e, tmp1
                a, c, d = a, d, c
                b, e, f = b, e, tmp2
            elif i == "E":
                tmp1, tmp2 = a, c
                a, c, f = c, f, a
                a, d, e = a, e, d
                a, c, f = a, f, tmp2
            elif i == "W":
                tmp1, tmp2 = a, d
                a, c, f = c, f, a
                a, d, e = a, e, d
                a, c, f = a, f, tmp1
            elif i == "S":
                tmp1, tmp2 = a, e
                a, b, e = e, f, a
                a, e, d = a, d, e
                a, b, e = a, e, tmp2
    return is_right_surface
    
a, b, c, d, e, f = map(int, input().split())
dice = Dice(a, b, c, d, e)
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    print(is_right_surface(x, y)[0])