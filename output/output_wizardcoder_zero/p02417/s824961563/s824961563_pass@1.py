a = input() + str(input())
while True:
    try:
        a += input().lower()
    except EOFError:
        break
for i in range(ord('a'), ord('z')+1):
    count = 0
    print(chr(i) + ': ', end=' ')
    for j in range(len(a)):
        if a.count(chr(i)) > count:
            count = a.count(chr(i))
print(count)

# This code reads one line of input at a time and concatenates it with the previous input to form the final string, making sure that all inputs are lowercase. Then, it iterates through each character in the string and counts its occurrences for each letter, using ord() to convert the letters to their ASCII values and chr() to convert them back to characters. It prints out each count on a new line after computing it.