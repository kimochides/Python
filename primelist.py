num1=int(input("Enter the starting number:"))
num2=int(input("Enter the ending number:"))
count=0
for i in range(num1,num2+1):
    for num in range(2,i):
        if i%num==0:
            break
    else:
        print(i)
        count=count+1
print("Total number of prime numbers:",count)
