alphabet='abcdefghijklmnopqrstuvwxyz'
count_dict = {}

for char in alphabet:
  count_dict[char] = 0

input_string = ''.join(sys.stdin.read().lower()) #convert input to lowercase and join all characters into a string

for char in input_string:
  if char in alphabet:
    count_dict[char] += 1

for char, count in count_dict.items():
  print(f"{char}: {count}")