r=int(input("Enter the number of elements in the array: "))
a=list(map(int,input("Enter the elements of the array: ").split()))
sort=sorted(a)
print("The largest element:", a[-1])