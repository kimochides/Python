def rev(str):
    rev=""
    i=len(str)-1
    while i>=0:
        rev=rev+str[i]
        i-=1
    return rev
strin=input("Enter a string to be reversed:")
revstr=rev(strin)
print("Revered string:",revstr)

