m1=int(input("Enter marks 1:"))
m2=int(input("Enter marks 2:"))
m3=int(input("Enter marks 3:"))
s1=(m1+m2)/2
s2=(m2+m3)/2
s3=(m1+m3)/2
if(s1>s2 and s1>s3):
    h=s1
elif(s2>s3 and s2>s1):
    h=s2
else:
   h=s3
print("Highest score is:",h)
