def factorial(a):
    sum=1
    for i in range(a,1,-1):
        sum=sum*i
    return sum
a=int(input("Enter a number:"))
temp=a
add=0
while(temp>0):
    digit=temp%10
    add=add+factorial(digit)
    temp=temp//10
if add==a:
    print("Peterson Number")
else:
    print("Not a Peterson Number")