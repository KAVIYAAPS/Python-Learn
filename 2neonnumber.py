a=int(input("Enter a number:"))
square=a*a
sum=0
temp=square
while temp>0:
    digit=temp%10
    sum=sum+digit
    temp=temp//10
if sum==a:
    print("Neon Number")
else:
    print("Not Neon Number")