a=int(input("Enter a number:"))
b=a*2
c=a*3
con=str(a)+str(b)+str(c)
arr=list(map(int,con))
sort=sorted(arr)
og=[1,2,3,4,5,6,7,8,9]
if sort==og:
    print("Fascinating Number")
else:
    print("Not a Fascinating Number")
