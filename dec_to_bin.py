def dec_to_bin(d):
    if d==0:
        return "0"
    if d==1:
        return "1"
    b=""
    while d>0:
        b=str(d%2)+b
        d=d//2
    return b
d=int(input("Enter a decimal number:"))
b=dec_to_bin(d)
print("Binary representation:",b)