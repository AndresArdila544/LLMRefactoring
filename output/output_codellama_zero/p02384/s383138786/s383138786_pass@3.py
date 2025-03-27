from collections import defaultdict

input_data = input().split(" ")
items = list(map(int, input_data))
dice = dict(zip(['T', 'S', 'E', 'W', 'N', 'B'], items))

def q1():
    controls = input().split(" ")
    for i in controls:
        dice["T"] = dice["S"], dice["B"], dice["N"], dice["T"]
        dice["S"] = dice["N"], dice["T"], dice["S"], dice["B"]
        dice["E"] = dice["W"], dice["T"], dice["E"], dice["B"]
        dice["W"] = dice["E"], dice["B"], dice["W"], dice["T"]
    print(dice["T"])

def q2():
    repeater = int(input())
    for _ in range(repeater):
        control_input = input().split(" ")
        conds = list(map(int, control_input))
        target_key = defaultdict(lambda: "W", {
            "T": "E",
            "S": "N",
            "E": "B",
            "W": "T",
            "N": "S",
            "B": "E"
        })[conds[1]]
        print(dice[target_key])

q2()