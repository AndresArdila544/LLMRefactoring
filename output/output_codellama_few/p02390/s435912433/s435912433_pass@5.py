def convert_seconds_to_time(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    seconds = seconds % 60
    return f"{hours}:{minutes}:{seconds}"