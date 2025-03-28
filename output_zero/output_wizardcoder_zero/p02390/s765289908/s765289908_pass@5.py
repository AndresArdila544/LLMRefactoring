while True:
    try:
        s = int(input())
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

h = s // 360
m = (s - h*360) // 60
sec = s - m * 60
print('{}:{:02d}:{:02d}'.format(h, m, sec))