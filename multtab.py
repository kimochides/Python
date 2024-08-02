n=int(input("Enter a number:"))
print("The multiplication table of",n,"is:")
for i in range(1,11):
    prod=n*i
    print(n,"x",i,"=",prod)