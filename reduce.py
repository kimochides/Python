from functools import reduce
#define a function to add two numbers
def add(x,y):
    return x+y
#define the original tuple
original_tuple=(1,2,3,4,5)
#reduce the tuple to a single value(sum of elements)
result=reduce(add,original_tuple)
print("Result of reducing the tuple:",result)