n=int(input("Enter a range(n x n):"))
for i in range(0,n):
    for j in range(0,n):
            if(j<=i):
                print(j+1,end=" ")
    print()