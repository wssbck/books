a_list = [0, 2, 4, 10]

# print a list
print (a_list)

# print a hot-modified version of another list
print ([element * 10 for element in a_list])

# can be used for constructing lists of tuples
print ([(element, element * 10) for element in a_list])