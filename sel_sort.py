def sel_sort(a):
    n=len(a)
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
arr=[10,30,20]
sel_sort(arr)
print(arr)