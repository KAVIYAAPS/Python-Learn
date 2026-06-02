r=int(input("Enter the number of mobile numbers: "))
a=list(map(int,input("Enter the mobile numbers: ").split()))
target=int(input("Enter the mobile number to be searched: "))
if target in a:
    print("Mobile number found at index:", a.index(target))
else:
    print("Mobile number not found")