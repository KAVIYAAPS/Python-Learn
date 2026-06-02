a=int(input("Enter a number:"))
square=a*a
last=square%10
if last==a:
    print("Automorphic")
else:
    print("Not Automorphic")