arr=[10,20,30,10]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            print("Duplicate value:", arr[i])