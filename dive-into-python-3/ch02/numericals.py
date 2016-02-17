from fractions import Fraction

# integers
i = 1
print(type(1))

# floats
f = 1.0
print(type(f))

# coercing floats to ints TRUNCATES instead of rounding
print(int(2.6))

# ** means rising to power of
print(2 ** 3)

# fractions
fr1 = Fraction(2, 4)
fr2 = Fraction(3, 9)

# arguments for fractions need to be integers
try:
	fr3 = Fraction(1.5, 6)
except TypeError as e:
  print( str(e) )