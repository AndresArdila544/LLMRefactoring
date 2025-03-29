def convert_time(s):
    h = int(s/360)
    s %= 360
    m = int(s/60)
    s %= 60
    return f"{h}:{m}:{int(s)}"

print(convert_time(input())) # call the function with user input as argument, and print the result.