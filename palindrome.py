a=input("Enter a word:")
arr=list(a)
rev=arr[::-1]
if a=="".join(rev):
    print("Palindrome")
else:
    print("Not a palindrome")