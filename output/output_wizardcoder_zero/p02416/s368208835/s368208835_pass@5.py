```python
s = input() # Get user input string until they enter '0' 
while s != '0':  
    print(sum(map(int, s)) # Convert input string to list of integers and sum them up using built-in map function. Print the result. 
    s = input() 
```

The code takes user input until they enter '0' and then calculates the sum of all the numbers in the input string by converting it into a list of integers using the `map` function and applying the built-in `sum` function on it.