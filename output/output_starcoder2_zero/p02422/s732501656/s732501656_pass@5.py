Original Code:

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    for n_itr in range(n):
        firstLast = input().split()

        firstName = firstLast[0]

        lastName = firstLast[1]


        print(firstName[0] + lastName[- 2:])