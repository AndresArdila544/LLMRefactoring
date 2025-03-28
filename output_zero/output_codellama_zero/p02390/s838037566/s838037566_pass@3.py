def convert_seconds_to_hms(S):
    h = S // (60*60)
    m = (S - (h*60*60)) // 60
    s = S % 60
    return f"{h:02d}:{m:02d}:{s:02d}"