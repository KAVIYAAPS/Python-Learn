r=int(input("Enter the number of elements in the array: "))
a=list(map(int,input("Enter the elements of the array: ").split()))
arr=set(a)
if len(arr)<2:
    print("There is no second largest element in the array.")
else:
    sort=sorted(arr)
    print("The second largest element is:", sort[-2])