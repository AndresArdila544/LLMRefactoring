import sys
from numpy import matrix


def main():
    # N and M are given on input
    try:
        n, m = [int(item) for item in sys.stdin.readline().split()]

        # A is given as a list of rows
        a = []
        while True:
            row = [int(item) for item in sys.stdin.readline().split()]
            if len(row) == 0:
                break
            else:
                a += [row]

        # B is given as a list of columns
        b = []
        while True:
            column = [int(item) for item in sys.stdin.readline().split()]
            if len(column) == 0:
                break
            else:
                b += [[item] for item in column]

    except ValueError:
        print("Error! Please enter integer values.")
        exit()


    # Calculate the product of A and B
    # The result is a list of columns which are then transposed into rows
    product = matrix(a).T * matrix(b)
    result = []

    # Convert numpy array into a list
    for row in range(len(product)):
        result += [list(product[row])]

    # Print the result
    for i in range(n):
        print(" ".join([str(elem) for elem in result[i]]))


if __name__ == '__main__':
    main()