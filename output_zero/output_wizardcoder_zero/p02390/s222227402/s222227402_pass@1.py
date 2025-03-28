def time_to_hms(seconds):
    h = seconds // 36000
    m = (seconds % 36000) // 60
    s = seconds % 60
    return f"{h}:{m}:{s}" 

print(time_to_hms(int(input()))