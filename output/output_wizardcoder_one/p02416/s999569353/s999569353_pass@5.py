```python
import math
x = input()
while True:
    x_list=[int(i) for i in str(x)]
    if int(x)>0:
        print(sum(x_list))
    else:
        break