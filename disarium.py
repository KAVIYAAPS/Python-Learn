first=input("Enter the number:")
a=list(map(int, first))
sum=0
for i in range(len(a)):
    sum=sum+a[i]**(i+1)
if sum==int(first):
    print("Disarium Number")
else:
    print("Not a Disarium Number")