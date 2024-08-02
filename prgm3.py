def counts(li,x):
    count=0
    for i in li:
            if i==x:
                count=count+1
    return count
li=[1,2,4,4,5,3,5,2,5,6,4]
print("The list is:",li)
x=int(input("Enter the element whose occurence is to be known:"))
print("Ocurrances of",x,"is",counts(li,x))
