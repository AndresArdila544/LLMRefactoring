<|start_of_text|><<

Python program:

    a = [int(e) for e in input().split()]
    print('a < b' if a[0]  < a[1] else 'a > b' if a[0]  > a[1] else 'a == b')


This is the first version of my refactored Python program, which does what it was supposed to do:

>>> 5 6 7 8 9
a < b