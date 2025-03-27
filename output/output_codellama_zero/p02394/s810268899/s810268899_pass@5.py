Here is the refactored version of your code:
w, h, x, y, r = map(int,raw_input().split())
if x>=r and x<=w-r and y>=r and y<=h-r:
    print "Yes"
else:
    print "No"

You may have noticed that I replaced the if/else statement with a simple print function.  This is because it simplifies the code by removing the need for multiple lines of code to accomplish one task, making it easier to read and understand what each line does.