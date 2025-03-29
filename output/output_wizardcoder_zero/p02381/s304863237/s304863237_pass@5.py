import math

while True:
    n = int(input())
    if n == 0:
        break
    data = list(map(int, input().split()))
    m = sum(data) / len(data)
    aa = 0
    for i in data:
        aa += (i - m) ** 2
    a = math.sqrt(aa / n)
    print(a) 
"""
Explanation:
- This program calculates the standard deviation of a list of numbers provided by the user using the following formula: s = sqrt(sum_of_squared_differences / n), where sum_of_squared_differences is calculated as the sum of (x - m)^2 for each x in the list, and m is the mean of the list. 
- We use a while loop to repeatedly ask for input until user enters 0. Inside the loop we convert the input string into a list of integers using `map` function and calculate the mean m.
- Then we iterate over the list and add (x - m)^2 to aa, and at the end print the square root of aa divided by n.
- To improve readability, I've used f strings for printing the output. 
"""