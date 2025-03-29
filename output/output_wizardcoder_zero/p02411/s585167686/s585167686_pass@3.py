new_list = []
while True:
    input_data = list(map(int, input().split()))
    if input_data == [-1, -1, -1]:
        break
    new_list.append(input_data)

for i in new_list:
    if i[0] == -1 or i[1] == -1:
        print("F")
    elif sum(i) >= 80:
        print("A")
    elif 59 < sum(i) < 80:
        print("B")
    elif 49 < sum(i) < 50 and i[2] >= 50:
        print("C")
    elif 49 < sum(i) < 50 and i[2] < 50:
        print("D")
    else:
        print("F")