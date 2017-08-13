'''
Slicing takes three parameters:

	- from
	- to
	- step

Slices can be expressed as [from:to:step] or slice(from, to, step).
In the second case, as slice objects, they can be named and reused,
in the following syntax: [slice_object].
'''

ls = [i for i in range(20)]
sl = slice(2, 10, 2)

'''
Both lines will print the same result
'''
print(ls[2:10:2])
print(ls[sl])
