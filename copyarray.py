r=int(input("Enter the number of elements in the array: "))
a=list(map(int,input("Enter the elements of the array: ").split()))
arr=[]
for i in range(r):
    arr.append(a[i])
print("The copy array:",arr)