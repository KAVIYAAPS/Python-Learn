a=int(input("Enter a num:"))
sum=0
for i in range(1,a):
    if(a%i==0):
        sum=sum+i
if(sum==a):
    print("Perfect")
else:
    print("Not Perfect")
