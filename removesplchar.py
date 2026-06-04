a=input("Enter a word:")
arr=list(a)
spl=["!","@","#","$","%","^","&","*","(",")","-","+","=","/","?","<",">",",",".",":",";","_"]
for i in range(len(arr)):
    if arr[i] not in spl:
        print(arr[i],end="")
    else:
        continue
    