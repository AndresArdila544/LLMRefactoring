```python
def main():
    i = 0
    while True:
        x = input()
        if x == "0":
            break
        print("Case {}: {}".format(i,x))
        i += 1
main()