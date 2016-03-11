# catching errors in import
try:
  import nonexisting_module
except ImportError:
  chardet = None

print(chardet)

# raising an error
raise ValueError('some value error')
