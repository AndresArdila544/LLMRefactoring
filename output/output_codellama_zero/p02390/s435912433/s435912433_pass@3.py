Here is a cleaner and more concise version of your program:
```
a = int(input())
print("{:02d}:{:02d}:{:02d}".format(*(a//3600, (a%3600)//60, (a%3600)%60)))
```