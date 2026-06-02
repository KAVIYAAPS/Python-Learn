a=list(map(int,input("Enter a number:")))
while len(a)>1:
    sum=0
    for i in range(len(a)):
        sum=sum+a[i]**2
    a=list(map(int,str(sum)))
if a[0]==1:
    print("Happy Number")
else:
    print("Not a Happy Number")