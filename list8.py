#sorted based on how close a number is to 50
#customised sort
def fun(n):
    return abs(n-50)
thislist=[100,50,65,82,23,49,48]
thislist.sort(key=fun)
print(thislist)