a=int(input("Enter a num:"))
square=a*a
last=square%10
if(a==last):
    print("Automorphic")
else:
    print("Not Automorphic")