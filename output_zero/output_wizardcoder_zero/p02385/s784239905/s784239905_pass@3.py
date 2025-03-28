def roll_dice(direction):
    def move_south():
        return [numbers[0]] + numbers[:-2] + [numbers[-1], numbers[-3], numbers[-2]]

    def move_north():
        return numbers[2:] + [numbers[0], numbers[1]]

    def move_east():
        return numbers[-4:] + numbers[:2]

    def move_west():
        return numbers[2:] + numbers[:4][::-1]

    def map_values():
        nonlocal dice_numbers, vertical, horizontal
        for i in range(6):
            if not i % 2:
                vertical = [numbers[0]] * 3 + [numbers[-1], numbers[1], numbers[4], numbers[-2]]
                horizontal = [numbers[3], numbers[0], numbers[5], numbers[1]]
            else:
                vertical = numbers[:3] + [numbers[0], numbers[2], numbers[-1], numbers[5]]
                horizontal = [numbers[4], numbers[0], numbers[3], numbers[1]]
        return dice_numbers, vertical, horizontal

    def check_match(dice):
        nonlocal flag
        for i in range(6):
            if dice.vertical == target_vertical:
                if dice.horizontal == target_horizontal:
                    flag = True
                    break
            else:
                roll_dice("SWN")
        roll_dice("N")

    dice1 = Dice([int(x) for x in input().split()])
    dice2 = Dice([int(x) for x in input().split()] if not flag else dice1.numbers
    target_vertical, target_horizontal = [dice1.vertical[0], *dice1.vertical[1:]], [*dice1.horizontal[:2], *dice1.horizontal[-2:]]

    while not flag:
        check_match(dice1)
        dice1.numbers = roll_south() if direction == "N" else (roll_north() if direction == "S" else (roll_east() if direction == "E" else roll_west())
    print("Yes" if flag else "No")