"""


def get_next_int():
    return int(input())


x = get_next_int()
count = 1
while x != 0:
    print("Case {}: {}".format(count, x))

    count += 1
    x = get_next_int()