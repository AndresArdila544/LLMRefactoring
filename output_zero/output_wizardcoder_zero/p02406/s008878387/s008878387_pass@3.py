n = int(input())
print(' '.join([str(i) for i in range(1, n+1) if i%3==0 or '3' in str(i)] + ['\n'])
"""
Explanation: The original code takes an input integer `n` from the user and iterates through all integers from 1 to `n`. If the current integer is divisible by 3 or contains a `'3'` character in its string representation, it prints it on the same line. Finally, it prints a newline character at the end of the output.

The refactored version uses a list comprehension to generate a list of integers that meet the condition and joins them with spaces using `join()` method before printing the newline character.