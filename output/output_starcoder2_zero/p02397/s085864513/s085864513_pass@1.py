<|start_of_summary|> The program is designed to repeatedly prompt the user for an input of two integers separated by a space. If they enter 0 0 (zero followed by zero), it will then stop and exit the program, otherwise it will print out the numbers in ascending order separated by spaces. This is how you run this program:
$ python problem4.py
> 16 22
> 16 22
> 22 35
> 22 35
> 35 90
> 35 90
> 90 876
> 90 876
> 876 4
> 876 4
> 4 0
> 4 0
The input is always two integers separated by a space. If they are both zero, the program will terminate and exit. Otherwise, the output will be printed with each line being a pair of numbers separated by spaces in ascending order. In this case, it is:
16 22
22 35
35 90
876 4
0 4
I would like to know how I can improve the following code so that it fits better with Python's conventions and style guidelines:
while True:
    a = map(int,raw_input().split())
    if a == [0, 0]: break
    for x in sorted(a):
        print x,
This is what my solution looks like:
<|start_of_text|>