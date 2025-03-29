def print_pattern(N):
    if N[0] + N[1]: #checks if height and width are non-zero values
        for i in range(N[0]): #iterates over height of pattern
            if i == 0 or i == (N[0] - 1): #if first or last row
                print("#" * N[1]) #prints width number of '#' characters
            else:
                print("#", end="") #start with a '#' character
                for j in range(1,N[1]-2): #iterates over all but first and last columns
                    print(".", end="") #prints a '.' character between '#' characters
                if N[0] > 2: #if there are more than 2 rows (i.e., not the last row)
                    print("#") #moves to next line
                else:
                    pass #do nothing if it's the last row 
judge = True
while judge:
    N = list(map(int,input().split()))
    if not N[0] + N[1]: #checks for non-zero values in both height and width
        judge = False #ends loop
    else:
        print_pattern(N) 
        print() #moves to next line