import sys
def main():
    while True:
        h,w = map(int,input().split())
        if h==0 and w==0:
            break
        print('\n'.join(['#'*w,'.'*w+'.'*h, '.'*(w-2)+'.'+'#'*w] * (h//4)) if h%2 else print('\n'.join(list('##.') + ['#']*(w-2) + ['.##'])* (h//4)))
if __name__ == '__main__':
    #sys.stdin = open('input.txt', 'r')
    main()