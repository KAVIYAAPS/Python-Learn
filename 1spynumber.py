a=list(map(int,input("Enter a number:")))
sum=0
prod=1
for i in range(len(a)):
    sum=sum+a[i]
    prod=prod*a[i]
if sum==prod:
    print("Spy Number")
else:
    print("Not Spy Number")
       