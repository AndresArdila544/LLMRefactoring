def change_case(text):
    return ''.join([v.lower() if v.isupper() else v.upper() for v in text])