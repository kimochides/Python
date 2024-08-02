def yon(arr,n,x):
    arr.sort()
    l=0
    r=n-1
    while(l<r):
        if arr[l]+arr[r]==x:
            return True
        elif arr[l]+arr[r]>0:
            r=r-1
        else:
            l=l+1
    
    return False
n=5
x=3
arr=[1,-1,2,4,8]
res=yon(arr,n,x)
if res:
    print("Yes")
else:
    print("No")
