a_list = [1, -1, 2]

# generate a dictionary using list complehension
a_dict = { v:abs(v) for v in a_list }

print(a_list)
print(a_dict)

# dictionary keys as a set
print(set(a_dict.keys()))

# dictionary values as a set
print(set(a_dict.values()))

# dictionary items
print(list(a_dict.items()))

# dictionary comprehension
print({ element:element * 100 for element in a_list })

# create dictionary using dictionary comprehension
# swapping keys with values
a_second_dict = { 'a': 1, 'b': 2 }
print(a_second_dict)
print({ value:key for key, value in a_second_dict.items() })