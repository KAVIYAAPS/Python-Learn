a=list(map(int,input("Enter a number:")))
if a[0]!=0:
    for i in range(1,len(a)):
        if a[i]==0:
            print("Duck Number")
            break
        else:
            print("Not a Duck Number")
            break
else:
    print("Not a Duck Number")