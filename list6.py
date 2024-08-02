#based on a list of fruits, you want a new list containing only the fruits with the letter a in it
list=["apple","banana","cherry","kiwi","mango"]
newlist=[]
for x in list:
    if "a" in x:
        newlist.append(x)
print(newlist)
#with the help of list comprehension:
newlist1=[x for x in list if "a" in x]
print(newlist1)