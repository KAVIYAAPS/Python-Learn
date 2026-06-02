def getNumber():
    a=int(input("Enter a number: "))
    return a
sum=0
a=getNumber()
while(a!=0):
    sum+=a
    a=getNumber()
print("The sum is: ",sum)
   