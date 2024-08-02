tuple_of_integers=(5,2,8,1,3)
sorted_tuple=tuple(sorted(tuple_of_integers))
print("Original tuple:",tuple_of_integers)
print("Sorted tuple:",sorted_tuple)

#tuple comprehension to create a tuple of squares:
squares_tuple=tuple(x**2 for x in range(1,6))
print("Squares tuple:",squares_tuple)

