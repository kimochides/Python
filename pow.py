def pow(n,p):
    if(p==1):
        return n
    temp=pow(n,p//2)
    if(p%2!=0):
        return n*temp*temp
    else:
        return temp*temp
N=int(input("Enter a value:"))
P=int(input("Enter it's power:"))
res=pow(N,P)
print(N,"^",P,"=",res)