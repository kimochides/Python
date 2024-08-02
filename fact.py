num=int(input("Enter a number:"))
while(num!=0):
    f=1
    i=1
    while(i<=num):
        f=f*i
        i=i+1
    print("Factorial of",num,"is",f)
    break
if(num<0):
    print("INVALID")
if(num==0):
    print("Factorial of 0 is 1")