You can simplify this program by using a dictionary to map the operators to their corresponding arithmetic functions instead of using if-else statements for each operator. This way, you can avoid repeating the same code over and over again and make it more concise and readable. Here's the refactored version:


```python
while True:
    a, op, b = input().split()
    
    if op == "?":  # If operator is '?' break loop
        break
    else:      
        a, b = int(a), int(b) # Convert inputs to integers
        operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y}  # Define dictionary of operators with lambda functions for arithmetic operations
        result = operators[op](a, b) # Use operator to perform arithmetic operation on inputs and store in variable
        print(result)
```

This is the cleanest and most concise version I can think of. It defines a dictionary of lambda functions that take two parameters and return their result when evaluated with the input values `a` and `b`. The operator is used as a key to select the appropriate function from the dictionary, which is then applied to those inputs to produce the arithmetic operation's output.