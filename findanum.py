r=int(input("Enter the number of elements in the array: "))
a=list(map(int,input("Enter the elements of the array: ").split()))
target=int(input("Enter the target number: "))
if target in a:
    print("The target number is present in the array.")
else:
    print("The target number is not present in the array.")