def armstrong(i):
    temp=i
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**len(str(i))
        temp=temp//10
    return sum==i
n=int(input("Enter a range:"))
for i in range(1,n+1):
    if armstrong(i):
        print(i)
    