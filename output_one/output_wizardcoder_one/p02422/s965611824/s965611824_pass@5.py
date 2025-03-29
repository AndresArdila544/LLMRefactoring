```python
def perform_operation(s: str, operations: list):
    for operation in operations:
        if operation[0] == 'replace':
            s = s[:int(operation[1])] + operation[3] + s[int(operation[2])+1:]
        elif operation[0] == 'reverse':
            start, end = int(operation[1]), int(operation[2])
            s = s[:start] + s[start:end+1][::-1] + s[end+1:]
        elif operation[0] == 'print':
            print(s[int(operation[1]):int(operation[2])+1])

def main():
    string = input()
    operations = []
    for _ in range(int(input())):
        operation = input().split()
        operations.append(operation)
    perform_operation(string, operations)
```