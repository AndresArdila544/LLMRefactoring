# Cleaner version of the program
num = int(input())
print(" ".join([str(i) if i % 3 == 0 else str(i) + " " for i in range(1, num+1) if "3" in str(i)]))