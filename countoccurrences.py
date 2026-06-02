r=int(input("Enter the number of elements: "))
a=list(map(int,input("Enter the elements: ").split()))
c=int(input("Enter the element to count occurrences: "))
count=0
for i in range(r):
    if a[i]==c:
        count+=1
    else:
        continue
print("The number of occurrences of", c, "is:", count)
