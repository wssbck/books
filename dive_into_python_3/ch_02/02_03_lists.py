# Creating a list
a_list = [2, 'a', 2, True, 'something', ['nested list']]
print(a_list)

# Accessing elements, using positive and negative indices
print(a_list[2])
print(a_list[-1])

# Slicing a list
print(a_list[1:3])
print(a_list[1:-1])
print(a_list[:-1])

# Extending a list
a_list += [ 'add this' ]
a_list.append( 3.14 )           # Add one element to a list
a_list.extend([ 'one', 'two' ]) # Add multiple elements from another list
print(a_list)

# Looking for elements in a list
print(a_list.count( 2 ))
print(a_list.index( 2 )) # Only the index of the first occurence is returned

# Removing items from a list
del a_list[1]
print(a_list)
# Will throw an error if the element is not present in the list
a_list.remove(2)
print(a_list)
# Will throw an error if popping from an empty list
a_list.pop()
print(a_list)

# Boolean context
print(bool( [] ))
print(bool( [[]] ))
print(bool( [['a'], 2] ))
print(bool( [False] ))