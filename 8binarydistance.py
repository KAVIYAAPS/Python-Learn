a=int(input("Enter a number:"))
b=bin(a)[2:]
c=list(map(int,str(b)))

for i in range (len(c)):
    if c[i]==1 and c[i+1]==1:
        print(i)
    else:
        continue
        
