#removes the first occurance of an element from the list
list=["apple","banana","cherry","banana"]
list.remove("banana")
print(list)
#removes the element at the specified index:pop
list1=["apple","banana","cherry"]
list1.pop(1)
print(list1)
#delete del keyword removes the element of the specified index, and can remove the entire list as well
list2=["apple","banana","cherry"]
del list2[0]
print(list2)
del list2
print(list2)
#clear method empties the list
list3=["apple","banana","cherry"]
list3.clear()
print(list3)