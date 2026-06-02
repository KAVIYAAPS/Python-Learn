r=int(input("Enter the number of elements in the array: "))
a=list(map(int,input("Enter the elements of the array: ").split()))
print("The og array:",a)
print("The rev array:",a[::-1])