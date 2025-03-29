```python
import math
x = input()
while x != "":
    x_list = [int(i) for i in str(x)]
    print(sum(x_list))
    x = input()
```