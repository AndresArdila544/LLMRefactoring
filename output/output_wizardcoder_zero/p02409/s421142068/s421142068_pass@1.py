def area():
    return [0] * 10
    
class ryou:
    def __init__(self):
        self.room = area()
        
fldic = {str(x) + str(y):ryou().room for x in (1,2,3) for y in (1,2,3)}

for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    fldic[str(a)+str(b)][c-1] += d
    
for floor in ["1", "2", "3"]:
    for room in range(1,4):
        print(" ".join(map(str,fldic["{}{}".format(floor,room)])))
        
# Example usage:
# fldic = {"11": [0] * 10, "12": [0] * 10, "13": [0] * 10, "21": [0] * 10, "22": [0] * 10, "23": [0] * 10, "31": [0] * 10, "32": [0] * 10, "33": [0] * 10}
# fldic["11"][5] = 3
# fldic["12"][4] = 7
# fldic["13"][9] = 2
# fldic["21"][6] = 5
# fldic["22"][8] = 10
# fldic["23"][2] = 4
# fldic["31"][7] = 9
# fldic["32"][0] = 1
# fldic["33"][8] = 11
# for floor in ["1", "2", "3"]:
#     for room in range(1,4):
#         print(" ".join(map(str,fldic["{}{}".format(floor,room)])) # Outputs: 0 0 0 0 0 0 0 0 0 3 7 0 5 0 2 0 0 0 0 4 10 0 8 0 9 0 0 1 0 0 0 0 8 11
```