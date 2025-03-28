B = ["#"*150, "."*150]
for i in range(0, len(XS), 2):
    print("".join([B[i%2][:int(XS[i+1])]))
    if XS[i] == 0 and XS[i+1] == 0: break