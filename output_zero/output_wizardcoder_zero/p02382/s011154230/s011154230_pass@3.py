```python
def custom_dist(A_lst, B_lst):
    return (sum([abs(a - b) ** p for a, b in zip(A_lst, B_lst)]) / len(A_lst), [abs(a - b) for a, b in zip(A_lst, B_lst)].sort(), max(abs(a - b) for a, b in zip(A_lst, B_lst))


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split())
    
    for p in [1, 2, 3]:
        print("{:.6f}".format(custom_dist(A, B)[0] ** (1/p))
        custom_dist(A, B)[1].sort()
        print("{:.6f}".format(custom_dist(A, B)[2]))
    
main()
```