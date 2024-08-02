l1=["apple","banana","cherry","mango"]
l2=[10,20,30,40]
l3=[True,False]
l4=list(("Jack"))
l5=list(("Jack","John"))
l1[1]="Kiwi"
print(l1)
l1[1:3]=["Pineapple","Dates","x"]
print(l1)
#if you insert more than you replace
list=["apple","banana","cherry"]
list[1:2]=["blackcurrant","watermelon"]
print(list)
#insert less items than you replace
list1=["apple","banana","cherry"]
list1[1:3]=["watermelon"]
print(list1)