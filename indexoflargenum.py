r=int(input("Enter the number of elements in the list: "))
a=list(map(int,input("Enter the elements of the list: ").split()))
large=a[0]
ind=0
for i in range(1,r):
    if a[i]>large:
        large=a[i]
        ind=1
print("The largest element is in the index:", ind)