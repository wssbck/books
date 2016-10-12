a_set = set(range(5))

# generate new set using set comprehension
print({ v ** 3 for v in a_set })

# generate a list using set comprehension
print(list({ v + 1 for v in a_set }))

# generate a dictionary using set comprehension
print({ v:v * 2 for v in a_set })