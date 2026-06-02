def prime(n): #13(prime) -> 31(prime)
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

count=0

a=int(input("Enter a num:"))
prime(a)
if prime(a):
    count+=1

b=int(str(a)[::-1])
prime(b)
if prime(b):
    count+=1

if count==2 and a!=b:
    print("Emirp")
else:
    print("Not emirp")