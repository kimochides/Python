#binary search
def bin_search(arr,n,k):
    arr.sort()
    l=0
    r=n-1
    
    while(l<=r):
        m=l+(r-l)//2
        if arr[m]==k:
            return True
        elif arr[m]<k:
            l=m+1
        else:
            r=m-1
    return False
n=5
arr=[1,2,7,5,3]
k=7
res=bin_search(arr,n,k)
if res:
    print("Element found")
else:
    print("Element not found")

#WITH RECURSION:
def bin_search_rec(arr,k,l,r):
    arr.sort()
    if l>r:
        return False
    m=l+(r-l)//2
    if arr[m]==k:
        return True
    elif arr[m]<k:
        return(bin_search_rec(arr,k,m+1,r))
    else:
        return(bin_search_rec(arr,k,l,m-1))
arr=[1,2,7,5,3]
k=7
l=0
r=len(arr)-1
res=bin_search_rec(arr,k,l,r)
if res:
    print("Element found")
else:
    print("Element not found")