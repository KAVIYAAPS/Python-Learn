a=int(input("Enter a num:"))
sum=0
temp=a
while(temp>0):
    last=temp%10
    sum=sum+last
    temp=temp//10
if a%sum==0:
    print("Harshad")
else:
    print("Not Harshad")