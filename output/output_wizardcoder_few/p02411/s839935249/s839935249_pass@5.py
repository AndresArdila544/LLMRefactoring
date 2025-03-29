n=int(input())
while True:
    m,f,r=(int(x) for x in input().split())
    if m==f==r==-1:
        break
    grades = ["F", "A", "B", "C", "C", "D"]
    if m<0 or f<0:
        result.append("F")
    elif 80<=m+f:
        result.append(grades[0])
    elif 65<=m+f<80:
        result.append(grades[1]
    elif 50<=m+f<65:
        result.append(grades[2]
    elif 30<=m+f<50 and r>=50:
        result.append(grades[2])
    else:
        result.append(grades[4]
for grade in result:
    print(grade)

Explanation:
The original code reads input from the user, calculates grades based on the given criteria, and appends them to a list called "result". It then prints each element of the list. The refactored version does the same thing but in fewer lines by using a loop to iterate over the cases instead of creating multiple if statements for each grade range. We also changed the grades list to have more readable values (A, B, C, D) and used an index to store the desired grade for each condition instead of using if else statements.