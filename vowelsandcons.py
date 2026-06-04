a=input("Enter a word:")
arr=list(a)
vowels=0
cons=0
vow=["a","e","i","u","o"]
for i in range(len(arr)):
    if arr[i] in vow:
        vowels+=1
    else:
        cons+=1
print("Vowels:",vowels)
print("Consonants:",cons)
