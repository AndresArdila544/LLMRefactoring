Original Solution by "<NAME>"

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

m = float(input('Enter the mark of maths:'))
f = float(input('Enter the mark of Physics:'))
r = float(input('Enter the mark of computer science:'))

if m == -1 or f == -1 :
    print("F")
elif  m + f >=80 and (m, f) != (-1,-1):
    print("A+")
elif m + f>=65 and (m, f) !=(-1,-1):
    print("B")
elif m + f >= 50 and (m,f)!=( -1 ,-1 ):
     print('C')
elif m + f >=30 and r>=50:
    print('C')
else :print('F')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/