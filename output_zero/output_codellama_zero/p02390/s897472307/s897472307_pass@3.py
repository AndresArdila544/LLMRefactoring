Here is the refactored Python program:

print(str(int(a)/3600).zfill(2)+':'+str((int(a)%3600)/60).zfill(2)+':'+str(int(a)%60))