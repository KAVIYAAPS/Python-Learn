r=int(input("Enter the number of elements in the array: "))
a=list(map(int,input("Enter the elements of the array: ").split()))
sum=0
for i in range(r):
    sum+=a[i]
print("The sum of the array is: ",sum)