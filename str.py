str=input("Enter a string:")
n=len(str)
a=""
for i in range(0,n):
    if(i%2==0):
        a=a+str[i]
print(a)