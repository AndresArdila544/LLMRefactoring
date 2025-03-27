import sys
def main():
    while True:
        x = input()
        if x == '0':
            quit()
        print(sum([int(_) for _ in x]))

if __name__=='__main__':
    main()