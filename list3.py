#insert method inserts an item at the specific position
list=["apple","banana","cherry"]
list.insert(2,"watermelon")
print(list)
#to add an item at the end of the list
list1=["apple","banana","cherry"]
list1.append("watermelon")
print(list1)
#to append elements from another list to the current list
list2=["apple","banana","cherry"]
list3=["mango","pineapple","papaya"]
list2.extend(list3)
print(list2)