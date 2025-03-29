Here is a refactored version of your Python program that has fewer lines and improved readability:

n = input()
ai = [int(x) for x in raw_input().split()]
print min(ai), max(ai), sum(ai)