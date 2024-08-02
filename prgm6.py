li=[1,1,2,3,4,5,3,2,1,2,2,2,2,1,1,1]
count=0
newl=[]
k=int(input("Enter the frequency value:"))
for i in li:
    freq=li.count(i)
    if freq>k and i not in newl:
        newl.append(i)
print("List of elements with frequency greater than ",k,"is",newl)
#count is used to find the number of occurances or the count of a certain element.
