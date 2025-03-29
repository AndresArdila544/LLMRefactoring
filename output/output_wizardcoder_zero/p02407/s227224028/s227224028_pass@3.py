n = int(input())
word_list = input().split()
print(" ".join([str(word) for i in range(len(word_list)-1,-1,-1)])