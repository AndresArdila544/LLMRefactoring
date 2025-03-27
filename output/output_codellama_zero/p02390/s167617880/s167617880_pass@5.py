S = int(input())
print(f"{S//3600}:" + str((S//60)-(S//3600)*60).zfill(2) + ":" + str(S%60).zfill(2))