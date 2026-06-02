r=int(input("Enter the number of elements in the array: "))
a=list(map(int,input("Enter the elements of the array: ").split()))
sort=sorted(a)
for i in range(r-1):
    if sort[i]==sort[i+1] and sort[i] not in sort[:i]:
        print("The duplicate element is:", sort[i])
    else:
        continue