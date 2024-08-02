thisset={"apple","banana","cherry"}
thisset.add("orange")
print(thisset)

set={"apple","banana","cherry"}
tropical={"pineapple","mango","papaya"}
set.update(tropical)

set1={"apple","banana","cherry"}
list1=["kiwi","orange"]
set1.update(list1)
print(set1)

set2={"apple","banana","cherry"}
set2.remove("banana")
print(set2)

set2={"apple","banana","cherry"}
set2.discard("banana")
print(set2)

set3={"apple","banana","cherry"}
x=set3.pop()
print(x)
print(set3)

set4={"apple","banana","cherry"}
set4.clear()
print(set4)

del set3
print(set3)