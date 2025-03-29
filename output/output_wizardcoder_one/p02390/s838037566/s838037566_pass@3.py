def time_to_hms(seconds):
    h = seconds // (60*60)
    m = (seconds % 36000) // 60
    s = seconds % 60
    return f"{h}:{m}:{s}"

S = int(input())
print(time_to_hms(S))