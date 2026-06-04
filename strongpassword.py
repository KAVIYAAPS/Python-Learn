a=input("Enter a password: ")
if a[0].isupper() and len(a)>=8 and a.isalnum():
    print("Strong password")
else:
    print("Weak password")