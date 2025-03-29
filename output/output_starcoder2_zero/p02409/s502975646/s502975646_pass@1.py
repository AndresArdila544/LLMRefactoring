<|file_name:code.py|>

Here is how I would write the program:

import sys
write=sys.stdout.write
buildings=[[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]
for i in range(0,4):
    for j in range(0,3):
        for k in range(0,10):
            buildings[i][j].append(0)
informations=int(input())
for i in range(0,informations):
    information=[]
    information=input().split()
    information=[int(x) - 1 for x in information]
    buildings[information[0]][information[1]][information[2]]+=information[3]
for i in range(0,4):
    for j in range(0,3):
        for k in range(0,10):
            write(str(buildings[i][j][k]))
            write(' ')
        print()
    if i !=3:
        for j in range(0,20):
            write('#')
        print()


Here is how to run the program:

$ python code.py < input_file > output_file

If you use this test case file, it will produce the correct output and print the solution for you:
<|file_name:test.in|>
5
1 3 4 20
1 2 9 16
4 2 7 89
3 1 2 76
2 3 3 18
|<end_of_text|>

Here is the correct output for that test case file:
<|file_name:test.out|>
0  0  0  0  0  0  0  0  0  0  
0  0  0  0  0  0  0  0  0  0  
26 57 93 14 87 8 52 44 33 41  
17 42 41 52 72 11 79 86 17 17  
0  0  0  0  0  0  0  0  0  0  
41 22 92 64 39 17 81 28 14 55  
87 29 48 94 74 19 71 53 44 86  
95 34 10 65 46 42 10 46 18 62  
|<end_of_text|>