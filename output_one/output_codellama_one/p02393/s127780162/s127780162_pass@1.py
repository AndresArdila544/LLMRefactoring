import sys
def sort_and_print(lst):
    lst = map(int, input().split())
    print(" ".join([str(i) for i in sorted(lst)]))