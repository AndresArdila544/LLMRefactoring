"""


def input_int(prompt=None):
    return int(input(prompt))


def main():
    a = None

    while True:
        a = input()

        if "?" in a:
            break

        print(eval(a))


main()