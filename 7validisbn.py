a=list(map(int,input("Enter a num:")))
sum=0
if len(a)==10 or len(a)==13:
    for i in range (len(a)):
        sum=sum+a[i]*(i+1)
if sum%11==0:
    print("Valid ISBN")
else:
    print("Invalid ISBN")