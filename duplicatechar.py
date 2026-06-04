a=input("Enter a word:")
arr=list(a)
sort=sorted(arr)
for i in range(len(sort)-1):
    if sort[i]==sort[i+1] and sort[i] not in sort[:i]:
        print("Duplicate character:",sort[i])
    else:
        continue
