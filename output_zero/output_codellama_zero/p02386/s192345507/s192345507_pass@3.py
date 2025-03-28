class Dice:

    def __init__(self, labels):
        self.__pip = collections.Counter(labels)

    def roll_dice(self, c):
        if not self.__pip[c]:
            return False
        else:
            self.__pip[c] -= 1
            return True

    def get_top(self):
        return max(self.__pip, key=self.__pip.get)

    def get_front(self):
        return self.get_top() - 1

    def get_right(self):
        return self.get_front() + 1

    def get_left(self):
        return self.get_right() + 1

    def get_behind(self):
        return self.get_left() + 1

    def get_bottom(self):
        return self.get_behind() + 1

def main():
    n = int(input())
    *lst, = [input().split() for i in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            lst1 = lst[i]
            lst2 = lst[j]
            if len(set(lst1) ^ set(lst2)) != 0:
                break
            c = collections.Counter(lst2)
            dice1 = Dice(lst1)
            dice2 = Dice(lst2)
            dice2.roll_dice(c.most_common()[-1][0]) # 出現頻度の少ない数字の面を上にする
            if not dice1.judge(dice2):
                print('No')
                return
    print('Yes')

if __name__ == "__main__":
    main()