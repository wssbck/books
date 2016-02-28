# Tuples are immutable but work similarily to lists
a_tuple = ("a", "b", "mpilgrim", "z", "example")
print( a_tuple[0]   )
print( a_tuple[-1]  )
print( a_tuple[1:3] )

# The following would be an error:
# a_tuple.append("new")

# Immutability goes pair in pair with being more performant tha lists.
# It also allows to protect data that is not supposed to be changed.

# In boolean context:
def is_it_true(anything):
	if anything:
		print("yes, it's true")
	else:
		print("no, it's false")

is_it_true( a_tuple )
is_it_true( () )
is_it_true( (False,) )

# Warning! Parentheses with one element do not constitute a tuple.
# Python just assumes that it is an extra pair of parentheses.
print( type((False)) )
# A coma is needed. This seems silly at first.
print( type((False,)) )

# Using tuples for multple assignment
v = ('a', 2, True)
(x, y, z) = v
print(x)
print(y)
print(z)

# However it will not work if the number of values does not match
# v = ('a', 2, True, 'd')
# (x, y, z) = v
# w = (2,2)
# (x, y, z) = w

# An interesting example with range()
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print( MONDAY   )
print( SATURDAY )