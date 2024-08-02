def swaplist(li):
    size=len(li)
    temp=li[0]
    li[0]=li[size-1]
    li[size-1]=temp
    return li
li=[12,35,9,56,24]
print("Before swapping:",li)
swaplist(li)
print("After swapping:",li)
#swap elements given thier positions
def swapPositions(lis,pos1,pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp
    return lis
lis=[23,65,19,20]
pos1,pos2=1,3
print(swapPositions(lis,pos1-1,pos2-1))