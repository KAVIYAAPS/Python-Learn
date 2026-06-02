r=int(input("Enter the number of elements in the array: "))
a=list(map(int,input("Enter the elements of the array: ").split()))
arr=set(a)
print("The array without duplicates are:", arr)