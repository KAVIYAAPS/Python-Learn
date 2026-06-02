r=int(input("Enter the number of elements: "))
a=list(map(int,input("Enter the elements: ").split()))
target=int(input("Enter the element to check first occurrence: "))
for i in range(r):
    if a[i]==target:
        print("The first occurrence of", target, "is at index:",i)
        break
    else:
        continue