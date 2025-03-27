Here is the refactored version of the code:

num = int(input())
result = " ".join(str(i) for i in range(1, num+1) if (i%3==0 or str(i).find("3")!=-1))
print(result)

This refactored code is more concise and has fewer lines of code. It uses a list comprehension to generate a list of strings containing the numbers that meet the criteria, and then joins them together using the " ".join() method. This makes it easier to read and maintain the code.