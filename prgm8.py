li1=[10,20,30,40,50,60,70,80,90,100]
li2=[20,40,60,80,100,120,140]
inter=[]
for i in li1:
    for j in li2:
        if i==j:
            inter.append(i)
print(inter)
li1.extend(li2)
union=[]
for x in li1:
    if x not in union:
        union.append(x)
print("Union of lists 1 and 2:",union)
print("Intersection of lists 1 and 2:",inter)
#OR
#Use 'and' and 'or' operators
#Union: L1 and l2
#Intersection: L1 or L2
#Set removes duplicates
li3=[10,20,30,40,50,60,70,80,90,90,100]
li4=[20,40,60,80,100,120,140]

