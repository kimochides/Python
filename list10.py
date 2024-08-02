li=[10,-10,20,-20,30,30]
print("FIRST ELEMENT:",li[0])
print("LAST ELEMENT:",li[len(li)-1])
sum=0
for x in li:
    sum=sum+x
avg=sum/len(li)
li.sort()
print("MINIMUM ELEMENT:",li[0])
print("MAXIMUM ELEMENT:",li[len(li)-1])
print("SUM:",sum)
print("AVERAGE:",avg)