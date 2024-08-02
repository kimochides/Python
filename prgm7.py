li=[3,6,9,12,15,18,21,24,27,30]
print("Given list is:",li)
n=int(input("Enter the starting range:"))
m=int(input("Enter the ending range:"))
res=[]
count=0
for x in li:
    if x in range(n,m+1):
        res.append(x)
        count=count+1
if count!=0:
    print("Elements of the list are present in the range.")
    print("Elements of list present in the range of",n,"to",m,"is:",res)
else:
    print("Elements of the list are not present in the range.")

