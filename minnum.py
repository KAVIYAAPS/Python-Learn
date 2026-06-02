r=int(input("Enter the number of elements in the list: "))
a=list(map(int,input("Enter the elements of the list: ").split()))
sort=sorted(a)
print("The smallest number in the list is:", sort[0])
