li=[2,3,5,4,2,5,6,3,4,5,9,7,6]
un=[]
count=0
for i in li:
    if i not in un:
        count=count+1
        un.append(i)
print("Unique elements in the list:",un,"\nCount of unique elements:",count)
