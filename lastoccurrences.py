r=int(input("Enter the number of elements in the list: "))
a=list(map(int,input("Enter the elements of the list: ").split()))
c=int(input("Enter the number to find the last occurrence of: "))
ind=-1
for i in range(r):
    if a[i]==c:
        ind=i
if ind==-1:
    print("The number", c, "is not found in the list.")
else:
    print("The last occurrence of", c, "is at index:", ind)