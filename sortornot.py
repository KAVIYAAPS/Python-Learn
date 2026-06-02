arr=[10,20,30]
array=sorted(arr)
count=0
for i in range(0,len(arr)):
    if arr[i]==array[i]:
        count=count+1
if count==len(arr):     
    print("Sorted")
else:    print("Not sorted")
