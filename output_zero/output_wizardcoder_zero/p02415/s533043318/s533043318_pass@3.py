s = input()
trans = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "bcdfghjkmnpqrtwxyzBCDFHJKLMQSVWXZabdegiklmnpruwx")
print(s.translate(trans))