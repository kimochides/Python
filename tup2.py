my_tuple=(1,2,3)
another_tuple=tuple([4,5,6])
print(my_tuple[0]) #accessing first element
print(my_tuple[-1]) #acessing last element
print(my_tuple[1:3]) #slicing to get a subset of the tuple

combined_tuple=my_tuple+another_tuple
print(combined_tuple)

repeated_tuple=my_tuple*3
print(repeated_tuple)

print(2 in my_tuple) #to check if 2 is in my_tuple. Here, 2 IS in my_tuple, hence, output is True
print(4 not in my_tuple) #to check if 4 is NOT in my_tuple. Output is False, as 4 is not in my_tuple
print(len(my_tuple)) #gives the length of the tuple. In this case, len(my_tuple)=3

for item in my_tuple:
    print(item)

string_to_tuple=tuple("hello")
print("String to tuple:",string_to_tuple)

list_to_tuple=tuple([1,2,3])
print("List to tuple:",list_to_tuple)

print(my_tuple.index(3)) #gives the index of 3 in tuple 'my_tuple'
print(my_tuple.count(2)) #gives the count of 2 found in tuple 'my_tuple'

