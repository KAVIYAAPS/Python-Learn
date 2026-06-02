a=list(map(int,input("Enter a num:")))
while len(a)>1:
    sum=0
    for i in range(len(a)):
        sum=sum+a[i]
    a=list(map(int,str(sum)))
if a[0]==1:
    print("Magic Number")
else:
    print("Not a Magic Number")