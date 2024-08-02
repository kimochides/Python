#PARAMETERS OR ARGUMENTS
#Default arguments:
def myfun(x,y=50): #in function defination, directly assign paramater y. Here, y is assigned to 50
    print("x=",x)
    print("y=",y)
myfun(10) #y parameter isn't passed in function call, thus, assign parameter y in function defination

#keyword arguments:
def student(firstname,lastname):
    print(firstname,lastname)
student(firstname="John",lastname="Snow")
student(lastname="Snow",firstname="John")

#non-keyworded variable length arguments:
def my_funct(*argv):
    print(argv)
#driver code
my_funct("Hello","Welcome","To","India",2.0)

#keywordedd variable length arguments:
def funct(**kwargs):
    print(kwargs)
#driver code
funct(a='Hello',b='World')
