def get_case(input):
    if input == 0:
        break
    print("Case {0}: {1}".format(count, x))
    count += 1

def main():
    while True:
        x = int(input())
        count = 1
        get_case(x)

main()