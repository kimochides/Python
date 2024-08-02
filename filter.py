original_tuple=(1,2,3,4,5)
filtered_tuple=tuple(filter(lambda x: x%2==0,original_tuple))
print("Filtered tuple:",filtered_tuple)