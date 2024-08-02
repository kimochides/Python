def prod(res):
    prod=1
    for i in res:
        prod=prod*i
    return prod
li=[1,2,3,1,2,3]
print("Original List:",li)
res=[]
[res.append(x) for x in li if x not in res]
print("List after removing duplicate elements:",res)
print("Duplication removal list product=",prod(res))