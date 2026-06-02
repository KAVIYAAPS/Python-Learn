def prime(a):
    if a<=1:
        return False
    for i in range (2,a):
        if a%i==0:
            return False
    return True
count=0
a=int(input("Enter a number:"))
if prime(a):
    count+=1

b=str(a)
for i in range (1,len(b)):
    rot=int(b[i:]+b[:i])
    if prime(rot):
        count+=1  
if count==len(b):
    print("Circular Prime")
else:
    print("Not Circular Prime")

