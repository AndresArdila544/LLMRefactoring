import math;a,b,c=map(float,input().split());print('\n'.join([*map('{:<0.4f}'.format,math.pi*s/180*(c+(2*math.atan(h/b))),l,h)]))

Here is a test case for the program:
<|test_cases|>
>>> Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import math;a,b,c=map(float,input().split());print('\n'.join([*map('{:<0.4f}'.format,math.pi*s/180*(c+(2*math.atan(h/b))),l,h)]))
6 9 35
13.1781
25.0000
5.8300
>>>