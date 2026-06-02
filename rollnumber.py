r=int(input("Enter the number of students: "))
a=list(map(int,input("Enter the roll numbers: ").split()))
target=int(input("Enter the roll number to be searched: "))
if target in a:
    print("Student found at index:", a.index(target))
else:
    print("Student not found")