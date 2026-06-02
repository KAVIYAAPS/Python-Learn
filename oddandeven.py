r=int(input("Enter the number of elements in the array: "))
a=list(map(int,input("Enter the elements of the array: ").split()))
count_odd=0
count_even=0
for i in range(r):
    if a[i]%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("Even:" ,count_even)
print("Odd:" ,count_odd)