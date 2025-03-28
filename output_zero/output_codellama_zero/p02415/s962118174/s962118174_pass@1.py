string = input()
print(*map(lambda x: x.upper() if x.islower() else x.lower() if x.isupper() else x, string), sep="")