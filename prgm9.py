li1=[20,80,50,40,70]
li2=[20,10,60,30]
print("List 1:",li1)
print("List 2:",li2)
li1.sort()
li2.sort()
li1.extend(li2)
un=[]
for x in li1:
    if x not in un:
        un.append(x)
print("Merged list is:",un)
un.sort()
print("Sorted merged list is:",un)
#another method: compare each element of list1 with list2, and append it to a merged list. However, if len(list1)!=len(list2), then append extra elements to the merged list.
#here, it's better to use while loop rather than for, as in for, we've to define the size, and the sizes of the two lists may be different, which may cause a list index out of range.
