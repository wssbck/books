import sys
import humansize

# everyhing is an object in Python, including functions
print(type(sys))
print(type(sys.path))
print(type(humansize))
print(type(humansize.approximate_size))

# even the type of an object is an object
print(type(type(sys)))

# functions are objects with some properties
# for example, doc string
print(type(humansize.approximate_size.__doc__))
print(humansize.approximate_size.__doc__)
