r=int(input("Enter range number: "))
a=list(map(int,input("Enter numbers: ").split()))
target=int(input("Enter target number: "))
for i in range(r):
    for j in range(i+1,r):
        if a[i]+a[j]==target:
            print("The numbers are: ",a[i],a[j])    
        else:
            continue