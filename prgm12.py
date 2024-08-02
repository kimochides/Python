def peak(lst):
    if not lst: #list is empty
        return None
    l,r=0,len(lst)-1
    while(l<r):
        mid=l+((l+r)//2)
        if(lst[mid]<lst[mid]+1):
            l=mid+1
        else:
            r=mid
    return lst[mid]
l=[1,1,2,1,3,5,6,4]
print("Peak:",peak(l))
