def large_sub_sum(lst):
    max_sum=cur_sum=lst[0]
    for i in lst[1:]:
        cur_sum=max(i,cur_sum+i)
        max_sum=max(max_sum,cur_sum)
    return max_sum
l=[1,3,-1,5,10,-12,-6,4,7,9]
print("Largest sub-array of the given array",l,"=",large_sub_sum(l))