```python
def main():
    x = int(input())
    print(x ** 3)

if __name__ == "__main__":
    main()
```
``` 
This program prompts the user to enter an integer, takes it as input and prints its cube. The original code is already concise and readable. However, if you still want a refactored version with fewer lines, you can remove the redundant "if __name__ == '__main__':" statement since the function will be executed when called directly anyway.

```python
def cube():
    x = int(input())
    print(x ** 3)

cube() # call this function to execute it.