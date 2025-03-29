while True:
    HM = input()
    if not HM: break #This line breaks the loop if user enters nothing.
    print("".join("#" * int(i)) for i in HM.split(" ") if i != 0) #Here we convert a string to a list, join each element of the list with the value of "#", and print the resulting list.