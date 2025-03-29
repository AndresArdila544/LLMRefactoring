refactored_version = lambda x: ''.join(str.upper(v) if str.islower(v) else str.lower(v) for v in input() if not str.isalpha(v))
print(refactored_version())