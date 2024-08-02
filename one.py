n=5
x=3
arr=[1,-1,2,4,8]
y=False
for i in range(n):
    for j in range(n):
        if arr[i]+arr[j]==x and i!=j:
            y=True
            break
    if y:
        break
if y==True:
    print("Yes")
else:
    print("No")
