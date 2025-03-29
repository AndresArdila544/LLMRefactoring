Here is what I need:
result=[]
while True:
    m, f, r=(int(x) for x in input().split())
    if(m==f==r==-1):
        break
    if m<0 or f<0:
        result.append("F")
    elif(m+f>=80):
        result.append("A")
    elif(m+f>=65):
        result.append("B")
    elif(m+f>=50):
        result.append("C")
    elif(m+f>=30):
        if(r>=50):
            result.append("C")
        else:
            result.append("D")
    else:
        result.append("F")
for grade in result:
    print(grade)


I need a refactored version of the code that requires fewer lines and improves readability while preserving its functionality. Please provide the refactored version with no explanations, introductions, or concluding remarks. Just give me the Python code, no quotations. Just the code.