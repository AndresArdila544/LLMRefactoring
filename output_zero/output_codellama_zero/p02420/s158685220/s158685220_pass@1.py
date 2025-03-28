def main():
    for line in sys.stdin:
        ls = line.strip('\n')
        if p == 0 and ls != '-':
            letters = ls
            p = 1
        elif p == 1:
            m = int(ls)
            p = 2
        elif p == 2:
            h = int(ls)
            letters = letters[h:] + letters[:h]
            if m > 1:
                m -= 1
            else:
                print letters
                p = 0

if __name__ == "__main__":
    main()