l1=["apple","banana","cherry","mango"]
l2=[10,20,30,40]
l3=[True,False]
l4=list(("Jack"))
l5=list(("Jack","John"))
print(l4)
print(l5)
print(l1[0])
print(l1[0:4])
print(l1[:4])
print(l1[0:])
print(l1[:])
#starting index should be less than or equal to the ending index
print(l1[-4:-1])
x=len(l1)
print(x)
print(type(l1))
print(type(l1[0]))
if "apple" in l1:
    print("Exists")

