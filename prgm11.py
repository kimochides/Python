def part_list(lst,pivot):
    less_than=[x for x in lst if x<pivot]
    equal_to=[x for x in lst if x==pivot]
    greater_than=[x for x in lst if x>pivot]
    return less_than+equal_to+greater_than
my_list=[3,1,4,1,5,9,2,6,5]
pivot_value=4
print("Partitioned list:",part_list(my_list,pivot_value))