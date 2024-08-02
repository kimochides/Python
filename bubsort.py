def bub_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:             #pushing heavy/large elements to the end of the array
                a[j],a[j+1]=a[j+1],a[j] #swapping
    return a
arr=[10,30,20,5,15]
print("Original Array:",arr)
sort=bub_sort(arr)

print("Sorted Array:",sort)
