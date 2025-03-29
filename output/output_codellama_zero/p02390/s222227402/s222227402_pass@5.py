Here is a refactored version of your original Python program that has fewer lines and improved readability:

S = int(input())
print("{}:{}:{}".format(*divmod(S, 3600)))