Here is the refactored version of the code:

orders = input().split()
if orders[0] == "replace":
    word = orders[3]
    t = t[:int(orders[1])] + word + t[int(orders[2])+1:]
elif orders[0] == "print":
    print(t[int(orders[1]) : int(orders[2])+1])
elif orders[0] == "reverse":
    t = t[:int(orders[1])]+t[int(orders[1]) : int(orders[2])+1][::-1]+t[int(orders[2])+1:]