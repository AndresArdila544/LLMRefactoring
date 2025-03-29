def count_chars(sentence):
    table = "abcdefghijklmnopqrstuvwxyz"
    sentence1 = sentence.lower()
    for char in table:
        print(char + ' : ' + str(sentence1.count(char)))

if __name__ == "__main__":
    count_chars(input())