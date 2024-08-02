#linear search
def lin_search(arr,k):
    n=len(arr)
    for i in arr:
        if i==k:
            return True
    return False
arr=[10,90,20,40,50]
k=20
res=lin_search(arr,k)
if res:
    print("Element found")
else:
    print("Element not found")