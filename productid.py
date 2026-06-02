r=int(input("Enter the number of products: "))
a=list(map(int,input("Enter the product IDs: ").split()))
target=int(input("Enter the product ID to be searched: "))
if target in a:
    print("Product found at index:", a.index(target))
else:
    print("Product not found")