### Hints:
Hint 1
The following is a good way to start:

    Use list comprehensions to create a list of only the male grades and a list of only the female grades
    Then check if all three lists are empty, in which case there are no students
        If so, break from the loop
    Otherwise, iterate through the M list and F list
        Use a conditional statement to determine the grade based on the average of their grades
    Output each grade

Hint 2
You can use the built-in function round() to round the averages. For example:

    average = sum(M) / len(M)
    print(round(average))





### Input Format:
The first line contains three integers, M F and R, which are the grades of three students. The values will be separated by a single space. If M is -1, F is -1 or R is -1, it indicates that there are no students left.

### Constraints:
M, F, and R are between 0 and 100.

### Output Format:
For each of the three grades, print the corresponding letter grade on a new line. These must be uppercase. If M is -1, F is -1 or R is -1, then output "F" (this happens only when there are no students left).
<|end_of_hints|>


### Sample Input:
    50 68 73
    42 90 -1
    -1 -1 -1


### Sample Output:
    C
    A
    F