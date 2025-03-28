hms = divmod(int(input()), 360)[::-1]
print('{}:{}:{}'.format(*map('{:02d}'.format, hms)) # using map() to format the output as two digits.