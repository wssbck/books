# catching errors in import
try:
  import nonexisting_module
except ImportError:
  chardet = None

# raising an error
raise ValueError('some value error')
