Here is the refactored version of the original program:

a, b, c = map(int, input().split())
ans = sum(i for i in range(a, b + 1) if c % i == 0)
print(ans)

The code has fewer lines and is more concise. The use of a list comprehension to generate the range of numbers instead of using the for loop makes the code more readable and easier to understand. Also, the use of the sum() function to count the number of divisors of c instead of using a separate variable makes the code more efficient.