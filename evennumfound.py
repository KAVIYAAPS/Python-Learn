r=int(input("Enter the number of elements in the list: "))
a=list(map(int,input("Enter the elements of the list: ").split()))
for i in range(r):
    if a[i]%2==0:
        print("Even number found")
        break
    else:
        print("Even number not found")
        break