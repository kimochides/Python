#UNION
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

set11={"a","b","c"}
set22={1,2,3}
set33=set11|set22
print(set33)

set4={"a","b","c"}
set5={1,2,3}
set6={"apple","banana","cherry"}
set7=set4.union(set5,set6)
print(set7)

#INTERSECTION
seti={"a","b","c"}
setii={"apple","banana","c"}
setiii=seti.intersection(setii)
print(setiii)

seti={"a","b","c"}
setii={"apple","banana","c"}
setiii=seti&setii
print(setiii)

#INTERECTION UPDATE
seti={"a","b","c"}
setii={"apple","banana","c"}
seti.intersection_update(setii)
print(seti)

#DIFFERENCE
set1={"a","b","c"}
set2={1,2,3}
set3=set1.difference(set2)
print(set3)

#DIFFERENCE UPDATE
set1={"a","b","c"}
set2={1,2,3}
set1.difference_update(set2)
print(set1)

#SYMMETRIC DIFFERENCE
set1={"a","b","c"}
set2={1,2,"c"}
set3=set1.symmetric_difference(set2)
print(set3)

#SYMMETRIC DIFFERENCE UPDATE
set1={"a","b","c"}
set2={1,2,"c"}
set1.symmetric_difference_update(set2)
print(set1)



