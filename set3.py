def power_sets(s):
    result=[[]]
    for ele in s:
        result.extend([subset+[ele] for subset in result])
    return [set(subset) for subset in result]

input_set={1,2,3}
powerset=power_sets(input_set)
print("Power set:",powerset)
