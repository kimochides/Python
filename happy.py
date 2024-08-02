def isHappy(num):
    sums=0
    while(num!=0):
        r=num%10
        sums=sums+r**2
        num=num//10
    return sums
n=int(input("Enter a number:"))
temp=n
while(n!=1 and n!=4):
    n=isHappy(n)
if(n==1):
    print("True")
elif(n==4):
    print("False")