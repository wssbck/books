# Sets are defined with curly brackets and contain unique values
a_set = {1, 2, 2, 2, 3}
print(a_set)

# Empty set must be created with set(), not curly brackets!
# For historical reasons, curly brakets mean empty dictionary
another_set = {}
print(type(another_set))
another_set = set()
print(type(another_set))

# Create a set from a list
a_list = [2, 3]
a_set  = set(a_list)
print(type(a_set))

# Adding values to a set
# .add adds one element
a_set.add(1)
a_set.add(1)
print(a_set)
# .update takes multiple sets or lists as paramaters
# and creates a union
a_set.update({2, 3, 4, 5, 5}, [1, 2, 6, 6, 2])
print(a_set)

# you can pop() from a set but since sets are not ordered,
# there is no control over which element is removed
print(a_set.pop())
print(a_set)

# is an element in a set?
print(3 in a_set)