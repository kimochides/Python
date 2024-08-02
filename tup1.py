def create_tuples():
    t1=(1,2,3,4,5)
    t2=("a","b","c","d","e")
    t3=("apple","banana","cherry")
    return t1,t2,t3

def access_tuple_items(tupl1,tupl2):
    print("Tuple 1:",tupl1)
    print("First element of tuple 1:",tupl1[0])
    print("Last element of tuple 1:",tupl1[-1])
    print("Tuple 2:",tupl2)
    print("First element of tuple 2:",tupl2[0])
    print("Last element of tuple 2:",tupl2[-1])
    print(tupl1[0:5])

def unpacking_tuple1(tuple3):
    (green,yellow,red)=tuple3
    print(green)
    print(yellow)
    print(red)

def unpacking_tuple2(fruits):
    fruits=("apple","banana","cherry","strawberry","raspberry")
    (green,yellow,*red)=fruits
    print(green)
    print(yellow)
    print(red)

def change_tuples(tuple1,tuple2):
    list1=list(tuple1)
    list2=list(tuple2)
    list1.append(6)
    list2.remove("c")
    tuple1=tuple(list1)
    tuple2=tuple(list2)
    return tuple1,tuple2

def loop_through_tuple(tuple1):
    print("Looping through tuple1 using a for loop:")
    for item in tuple1:
        print(item)
    print("\nLooping using while loop and index numbers:")
    index=0
    while index<len(tuple1):
        print(tuple1[index])
        index+=1

def join_tuples(tuple1,tuple2):
    #Joining tuples
    tuple3=tuple1+tuple2
    return tuple3

#main program:
tuple1,tuple2,tuple3=create_tuples()

access_tuple_items(tuple1,tuple2)
print()

unpacking_tuple1(tuple3)
print()

fruits=("apple","banana","cherry","strawberry","raspberry")
unpacking_tuple2(fruits)
print()

tuple1,tuple2=change_tuples(tuple1,tuple2)
print("After making changes:")
access_tuple_items(tuple1,tuple2)
print()

tuple3=join_tuples(tuple1,tuple2)
print("Joined tuple:",tuple3)


