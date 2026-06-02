a=list(map(int,input("Enter a number:")))
while len(a)>1:
    sum=0
    for i in range (len(a)):
        sum=sum+a[i]
    a=list(map(int,str(sum)))
if len(a)==1:
    print(sum)