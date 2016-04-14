# dictionaries are sets of key:value pairs
# on the outside similar to JSON objects
a_dict = {'a' : 1, 'b' : 2}
print(a_dict)
print(a_dict['a'])
element_b = 'b'
print(a_dict[element_b])

# dictionary keys are case sensitive
a_dict['B'] = 3
print(a_dict)

# assigning a new value to an existing key overwrites value on this key
a_dict['a'] = 56
print(a_dict)