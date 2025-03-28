'''

def main():

    text = input()
    count = int(input())
    for i in range(count):
        order = list(input().split())

        if order[0] == "replace":
            new_word = order[3]
            text = text[:int(order[1])] + new_word + text[int(order[2])+1:]
        
        elif order[0] == "print":
            print(text[int(order[1]): int(order[2]) + 1])

        elif order[0] == "reverse":
            text = text[:int(order[1])] + text[int(order[1]):int(order[2])+1][::-1]+ text[int(order[2])+1:]
main()